import json
import os

from dotenv import load_dotenv
from google import genai

from sqlalchemy.orm import Session

from app.models.interview import (
    InterviewSession,
    InterviewQuestion,
    InterviewAnswer,
    InterviewEvaluation,
)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================================
# Generate Evaluation using Gemini
# ==========================================================

def generate_evaluation_with_llm(
    session: InterviewSession,
    interview_data: list
):
    """
    Generate structured interview evaluation using Gemini.

    interview_data contains:
        question
        candidate_answer
        topic
        difficulty
        question_type
    """

    prompt = f"""
You are an expert technical interviewer and candidate evaluator.

Candidate Role:
{session.target_role}

Candidate Name:
{session.candidate_name or ""}

Interview Responses:
{json.dumps(interview_data, indent=2)}

Evaluate the candidate based on the interview responses.

IMPORTANT:

1. Evaluate ONLY the information provided.
2. Do not invent candidate skills.
3. Consider the candidate's actual answers.
4. Give scores from 0 to 100.
5. If an answer is empty, irrelevant, or meaningless, consider that when scoring.
6. Technical score should reflect technical correctness.
7. Problem-solving score should reflect reasoning and approach.
8. Communication score should reflect clarity and explanation.
9. Overall score should represent the overall interview performance.
10. Provide concise strengths.
11. Provide specific improvement areas.
12. Give a final recommendation.

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not add explanations outside JSON.

Required JSON format:

{{
    "overall_score": 0,
    "technical_score": 0,
    "problem_solving_score": 0,
    "communication_score": 0,
    "strengths": [],
    "improvement_areas": [],
    "summary": "",
    "recommendation": ""
}}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    # ------------------------------------------------------
    # Remove markdown code fences if Gemini returns them
    # ------------------------------------------------------

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)
        text = text.rsplit("```", 1)[0].strip()

    elif text.startswith("```"):
        text = text.replace("```", "", 1)
        text = text.rsplit("```", 1)[0].strip()

    try:
        evaluation = json.loads(text)

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Gemini returned invalid evaluation JSON:\n{text}"
        ) from e

    return evaluation


# ==========================================================
# Main Evaluation Function
# ==========================================================

def evaluate_interview(
    db: Session,
    session_id
):
    """
    Generate or retrieve the final evaluation for an interview.

    IMPORTANT:
    Only one InterviewEvaluation is allowed per session.

    If an evaluation already exists, return it instead of
    generating/inserting another evaluation.
    """

    # ======================================================
    # 1. Check whether evaluation already exists
    # ======================================================

    existing_evaluation = (
        db.query(InterviewEvaluation)
        .filter(
            InterviewEvaluation.session_id == session_id
        )
        .first()
    )

    if existing_evaluation:

        return existing_evaluation


    # ======================================================
    # 2. Get interview session
    # ======================================================

    session = (
        db.query(InterviewSession)
        .filter(
            InterviewSession.id == session_id
        )
        .first()
    )

    if not session:

        raise ValueError(
            "Interview session not found"
        )


    # ======================================================
    # 3. Get all interview questions
    # ======================================================

    questions = (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.session_id == session_id
        )
        .order_by(
            InterviewQuestion.question_number
        )
        .all()
    )


    # ======================================================
    # 4. Get all candidate answers
    # ======================================================

    answers = (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.session_id == session_id
        )
        .order_by(
            InterviewAnswer.question_number
        )
        .all()
    )


    # ======================================================
    # 5. Build question -> answer mapping
    # ======================================================

    answer_map = {
        answer.question_id: answer
        for answer in answers
    }


    # ======================================================
    # 6. Build evaluation input
    # ======================================================

    interview_data = []


    for question in questions:

        answer = answer_map.get(
            question.id
        )


        interview_data.append({

            "question_number":
                question.question_number,

            "topic":
                question.topic,

            "difficulty":
                question.difficulty,

            "question_type":
                question.question_type,

            "question":
                question.question,

            "candidate_answer":
                (
                    answer.candidate_answer
                    if answer
                    else ""
                )

        })


    # ======================================================
    # 7. Generate evaluation using Gemini
    # ======================================================

    evaluation_data = generate_evaluation_with_llm(
        session=session,
        interview_data=interview_data
    )


    # ======================================================
    # 8. Validate values
    # ======================================================

    overall_score = float(
        evaluation_data.get(
            "overall_score",
            0
        )
    )

    technical_score = float(
        evaluation_data.get(
            "technical_score",
            0
        )
    )

    problem_solving_score = float(
        evaluation_data.get(
            "problem_solving_score",
            0
        )
    )

    communication_score = float(
        evaluation_data.get(
            "communication_score",
            0
        )
    )


    strengths = evaluation_data.get(
        "strengths",
        []
    )

    improvement_areas = evaluation_data.get(
        "improvement_areas",
        []
    )

    summary = evaluation_data.get(
        "summary",
        ""
    )

    recommendation = evaluation_data.get(
        "recommendation",
        ""
    )


    # ======================================================
    # 9. Create evaluation record
    # ======================================================

    new_evaluation = InterviewEvaluation(

        session_id=session_id,

        overall_score=overall_score,

        technical_score=technical_score,

        problem_solving_score=problem_solving_score,

        communication_score=communication_score,

        strengths=strengths,

        improvement_areas=improvement_areas,

        summary=summary,

        recommendation=recommendation

    )


    db.add(
        new_evaluation
    )


    # ======================================================
    # 10. Commit
    # ======================================================

    try:

        db.commit()

        db.refresh(
            new_evaluation
        )

    except Exception:

        db.rollback()

        # --------------------------------------------------
        # Important:
        #
        # If two requests arrive simultaneously, both could
        # pass the "existing evaluation" check.
        #
        # PostgreSQL's unique constraint protects us.
        #
        # If another request inserted first, retrieve it.
        # --------------------------------------------------

        existing_evaluation = (
            db.query(InterviewEvaluation)
            .filter(
                InterviewEvaluation.session_id == session_id
            )
            .first()
        )

        if existing_evaluation:

            return existing_evaluation

        raise


    return new_evaluation
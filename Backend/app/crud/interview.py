import uuid

from datetime import datetime

from sqlalchemy.orm import Session

from app.models import (
    InterviewSession,
    InterviewQuestion,
    InterviewAnswer,
    ResumeData,
    ContextData
)


# ==========================================================
# INTERVIEW SESSION
# ==========================================================

def create_interview_session(
    db: Session,
    target_role: str,
    resume_filename: str | None,
    total_questions: int,
    candidate_name: str | None = None
):

    session = InterviewSession(

        candidate_name=candidate_name,

        target_role=target_role,

        resume_filename=resume_filename,

        status="in_progress",

        current_question=1,

        total_questions=total_questions

    )

    db.add(session)

    db.commit()

    db.refresh(session)

    return session


# ==========================================================
# GET INTERVIEW SESSION
# ==========================================================

def get_interview_session(
    db: Session,
    session_id: uuid.UUID
):

    return db.query(
        InterviewSession
    ).filter(
        InterviewSession.id == session_id
    ).first()


# ==========================================================
# SAVE RESUME DATA
# ==========================================================

def save_resume_data(
    db: Session,
    session_id: uuid.UUID,
    parsed_data: dict
):

    resume = ResumeData(

        session_id=session_id,

        parsed_data=parsed_data

    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume


# ==========================================================
# SAVE CONTEXT
# ==========================================================

def save_context(
    db: Session,
    session_id: uuid.UUID,
    context: dict
):

    context_record = ContextData(

        session_id=session_id,

        context=context

    )

    db.add(context_record)

    db.commit()

    db.refresh(context_record)

    return context_record


# ==========================================================
# SAVE QUESTIONS
# ==========================================================

def save_questions(
    db: Session,
    session_id: uuid.UUID,
    questions: list
):

    question_records = []

    for index, question_data in enumerate(
        questions,
        start=1
    ):

        question = InterviewQuestion(

            session_id=session_id,

            question_number=index,

            topic=question_data.get(
                "topic",
                ""
            ),

            difficulty=question_data.get(
                "difficulty",
                ""
            ),

            question_type=question_data.get(
                "type",
                ""
            ),

            question=question_data.get(
                "question",
                ""
            ),

            expected_skills=question_data.get(
                "expected_skills",
                []
            )
        )

        db.add(question)

        question_records.append(question)

    db.commit()

    for question in question_records:
        db.refresh(question)

    return question_records


# ==========================================================
# GET CURRENT QUESTION
# ==========================================================

def get_current_question(
    db: Session,
    session_id: uuid.UUID
):

    session = get_interview_session(
        db,
        session_id
    )

    if not session:
        return None

    question = db.query(
        InterviewQuestion
    ).filter(
        InterviewQuestion.session_id == session_id,
        InterviewQuestion.question_number == session.current_question
    ).first()

    return question


# ==========================================================
# SAVE ANSWER
# ==========================================================

def save_answer(
    db: Session,
    session_id: uuid.UUID,
    question_id: int,
    question_number: int,
    candidate_answer: str
):

    answer = InterviewAnswer(

        session_id=session_id,

        question_id=question_id,

        question_number=question_number,

        candidate_answer=candidate_answer,

        submitted_at=datetime.utcnow()

    )

    db.add(answer)

    db.commit()

    db.refresh(answer)

    return answer


# ==========================================================
# MOVE TO NEXT QUESTION
# ==========================================================

def advance_question(
    db: Session,
    session_id: uuid.UUID
):

    session = get_interview_session(
        db,
        session_id
    )

    if not session:
        return None


    # Don't move beyond the final question

    if session.current_question >= session.total_questions:

        return session


    session.current_question += 1

    db.commit()

    db.refresh(session)

    return session


# ==========================================================
# COMPLETE INTERVIEW
# ==========================================================

def complete_interview(
    db: Session,
    session_id: uuid.UUID
):

    session = get_interview_session(
        db,
        session_id
    )

    if not session:
        return None

    session.status = "completed"

    session.completed_at = datetime.utcnow()

    db.commit()

    db.refresh(session)

    return session


# ==========================================================
# GET ALL QUESTIONS
# ==========================================================

def get_session_questions(
    db: Session,
    session_id: uuid.UUID
):

    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.session_id == session_id
        )
        .order_by(
            InterviewQuestion.question_number
        )
        .all()
    )


# ==========================================================
# GET ANSWER FOR QUESTION
# ==========================================================

def get_answer_for_question(
    db: Session,
    session_id: uuid.UUID,
    question_id: int
):

    return (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.session_id == session_id,
            InterviewAnswer.question_id == question_id
        )
        .first()
    )



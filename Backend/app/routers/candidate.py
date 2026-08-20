from app.core.screening_config import (
    TOTAL_QUESTIONS,
    get_available_roles,
    is_available_role
)

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile,
    HTTPException,
    BackgroundTasks
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.interview import (
    CandidateEntryResponse,
    QuestionResponse,
    AnswerRequest,
    AnswerResponse,
    InterviewStatusResponse
)

from app.services.interview_service import (
    create_interview
)

from app.crud.interview import (
    get_interview_session,
    get_current_question,
    get_answer_for_question,
    save_answer,
    advance_question,
    complete_interview
)

from app.services.evaluation_background import (
    generate_evaluation_background
)


router = APIRouter(
    prefix="/candidate",
    tags=["Candidate"]
)





# GET AVAILABLE RECRUITMENT ROLES

@router.get("/roles")
def get_recruitment_roles():
    return {
        "roles": get_available_roles()
    }



# ==========================================================
# 1. Candidate Entry
# ==========================================================

@router.post(
    "/entry",
    response_model=CandidateEntryResponse
)
async def candidate_entry(

    file: UploadFile = File(...),

    role: str = Form(...),

    db: Session = Depends(get_db)

):

    # ======================================================
    # BACKEND CONNECTION
    #
    # Only roles with an available vector database are accepted.
    # ======================================================

    if not is_available_role(role):
        raise HTTPException(
            status_code=400,
            detail="Selected recruitment role is not available"
        )

    target_role = role


    result = create_interview(

        db=db,

        file=file,

        target_role=target_role

    )


    return result


# ==========================================================
# 2. Get Current Question
# ==========================================================

@router.get(
    "/{session_id}/question",
    response_model=QuestionResponse
)
def get_question(

    session_id: UUID,

    db: Session = Depends(get_db)

):

    # ======================================================
    # Get interview session
    # ======================================================

    session = get_interview_session(

        db,

        session_id

    )


    if not session:

        raise HTTPException(

            status_code=404,

            detail="Interview session not found"

        )


    # ======================================================
    # Check whether interview is completed
    # ======================================================

    if session.status == "completed":

        return QuestionResponse(

            completed=True,

            session_id=session.id,

            total_questions=TOTAL_QUESTIONS#session.total_questions

        )


    # ======================================================
    # Get current question
    # ======================================================

    question = get_current_question(

        db,

        session_id

    )


    if not question:

        raise HTTPException(

            status_code=404,

            detail="Question not found"

        )


    # ======================================================
    # Return current question
    # ======================================================

    return QuestionResponse(

        completed=False,

        session_id=session.id,

        question_id=question.id,

        question_number=question.question_number,

        total_questions=session.total_questions,

        topic=question.topic,

        difficulty=question.difficulty,

        question_type=question.question_type,

        question=question.question

    )


# ==========================================================
# 3. Submit Answer
# ==========================================================

@router.post(
    "/answer",
    response_model=AnswerResponse
)
def submit_answer(

    request: AnswerRequest,

    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db)

):

    # ======================================================
    # Get interview session
    # ======================================================

    session = get_interview_session(

        db,

        request.session_id

    )


    if not session:

        raise HTTPException(

            status_code=404,

            detail="Interview session not found"

        )


    # ======================================================
    # Don't allow answers after completion
    # ======================================================

    if session.status == "completed":

        raise HTTPException(

            status_code=400,

            detail="Interview is already completed"

        )


    # ======================================================
    # Get current question
    # ======================================================

    current_question = get_current_question(

        db,

        request.session_id

    )


    if not current_question:

        raise HTTPException(

            status_code=404,

            detail="Current question not found"

        )


    # ======================================================
    # Verify that candidate is answering the current
    # question
    # ======================================================

    if current_question.id != request.question_id:

        raise HTTPException(

            status_code=400,

            detail="This is not the current question"

        )


    # ======================================================
    # Validate answer
    # ======================================================

    if not request.answer.strip():

        raise HTTPException(

            status_code=400,

            detail="Answer cannot be empty"

        )


    # ======================================================
    # Prevent duplicate answer
    # ======================================================

    existing_answer = get_answer_for_question(

        db,

        request.session_id,

        request.question_id

    )


    if existing_answer:

        raise HTTPException(

            status_code=400,

            detail="Answer for this question already submitted"

        )


    # ======================================================
    # Save candidate answer
    # ======================================================

    save_answer(

        db=db,

        session_id=request.session_id,

        question_id=current_question.id,

        question_number=current_question.question_number,

        candidate_answer=request.answer

    )


    # ======================================================
    # Check if this was the last question
    # ======================================================

    if (

        current_question.question_number

        >= session.total_questions

    ):

        # ==================================================
        # Mark interview as completed
        # ==================================================

        complete_interview(

            db,

            request.session_id

        )


        # ==================================================
        # IMPORTANT
        #
        # Start evaluation immediately in the background.
        #
        # The candidate does NOT have to click
        # "View Evaluation Result" to start evaluation.
        #
        # The frontend receives the completed response
        # immediately.
        # ==================================================

        background_tasks.add_task(

            generate_evaluation_background,

            request.session_id

        )


        return AnswerResponse(

            success=True,

            next_question=None,

            completed=True

        )


    # ======================================================
    # Move to next question
    # ======================================================

    updated_session = advance_question(

        db,

        request.session_id

    )


    return AnswerResponse(

        success=True,

        next_question=updated_session.current_question,

        completed=False

    )


# ==========================================================
# 4. Interview Status
# ==========================================================

@router.get(
    "/{session_id}/status",
    response_model=InterviewStatusResponse
)
def get_status(

    session_id: UUID,

    db: Session = Depends(get_db)

):

    session = get_interview_session(

        db,

        session_id

    )


    if not session:

        raise HTTPException(

            status_code=404,

            detail="Interview session not found"

        )


    return InterviewStatusResponse(

        session_id=session.id,

        candidate_name=session.candidate_name,

        role=session.target_role,

        status=session.status,

        current_question=session.current_question,

        total_questions=session.total_questions

    )

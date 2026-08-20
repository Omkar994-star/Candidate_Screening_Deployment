from uuid import UUID

from app.core.database import SessionLocal

from app.services.evaluation_service import (
    evaluate_interview
)


def generate_evaluation_background(
    session_id: UUID
):
    """
    Generate interview evaluation in the background.

    A new database session is created because the database
    session used by the HTTP request should not be reused
    inside the background task.
    """

    db = SessionLocal()

    try:

        print(
            f"[EVALUATION] Starting evaluation "
            f"for session: {session_id}"
        )


        # ==================================================
        # Generate evaluation
        #
        # This function should:
        #
        # 1. Fetch questions
        # 2. Fetch candidate answers
        # 3. Send them to Gemini
        # 4. Generate evaluation
        # 5. Save evaluation to PostgreSQL
        # ==================================================

        evaluation = evaluate_interview(

            db=db,

            session_id=session_id

        )


        print(
            f"[EVALUATION] Evaluation completed "
            f"for session: {session_id}"
        )


        return evaluation


    except Exception as e:

        print(
            f"[EVALUATION] Failed for session "
            f"{session_id}: {e}"
        )


    finally:

        db.close()
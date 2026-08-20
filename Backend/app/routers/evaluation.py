from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.evaluation_service import (
    evaluate_interview
)


router = APIRouter(
    prefix="/candidate",
    tags=["Evaluation"]
)


# ==========================================================
# Generate / Get Evaluation
# ==========================================================

@router.post("/{session_id}/evaluate")
def evaluate_candidate(
    session_id: UUID,
    db: Session = Depends(get_db)
):

    try:

        evaluation = evaluate_interview(
            db=db,
            session_id=session_id
        )


        # ==================================================
        # Return evaluation to frontend
        # ==================================================

        return {

            "id": evaluation.id,

            "session_id":
                str(evaluation.session_id),

            "overall_score":
                evaluation.overall_score,

            "technical_score":
                evaluation.technical_score,

            "problem_solving_score":
                evaluation.problem_solving_score,

            "communication_score":
                evaluation.communication_score,

            "strengths":
                evaluation.strengths,

            "improvement_areas":
                evaluation.improvement_areas,

            "summary":
                evaluation.summary,

            "recommendation":
                evaluation.recommendation,

            "created_at":
                evaluation.created_at.isoformat()
                if evaluation.created_at
                else None

        }


    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
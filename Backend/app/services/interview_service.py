import os
import shutil

from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.crud.interview import (
    create_interview_session,
    save_resume_data,
    save_context,
    save_questions
)

from rag.resume_text_extractor import extract_text
from rag.llm_resume_parser import parse_resume_with_llm
from rag.context_construction import build_context
from rag.knowledge_retrieve import retrieve_knowledge
from rag.question_generator import generate_questions


UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ==========================================================
# CREATE INTERVIEW
# ==========================================================

def create_interview(
    db: Session,
    file: UploadFile,
    target_role: str
):

    # ======================================================
    # 1. Save Resume
    # ======================================================

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    try:

        # ==================================================
        # 2. Extract Resume Text
        # ==================================================

        resume_text = extract_text(
            file_path
        )

        if not resume_text:

            raise ValueError(
                "Could not extract text from resume."
            )


        # ==================================================
        # 3. Parse Resume using Gemini
        # ==================================================

        parsed_data = parse_resume_with_llm(
            resume_text=resume_text
        )


        # ==================================================
        # 4. Build Interview Context
        # ==================================================

        context = build_context(
            target_role,
            parsed_data
        )


        # ==================================================
        # 5. Retrieve Knowledge from FAISS
        # ==================================================

        knowledge = retrieve_knowledge(
            context,
            role=target_role
        )


        # ==================================================
        # 6. Generate Questions
        # ==================================================

        generated_questions = generate_questions(

            context,

            knowledge,

            parsed_data,

            target_role

        )


        questions = generated_questions.get(
            "questions",
            []
        )


        if not questions:

            raise ValueError(
                "No interview questions were generated."
            )


        # ==================================================
        # 7. Get Candidate Name
        # ==================================================

        candidate_name = parsed_data.get(
            "candidate_name",
            ""
        )


        # ==================================================
        # 8. Create Interview Session
        # ==================================================

        session = create_interview_session(

            db=db,

            target_role=target_role,

            resume_filename=file.filename,

            total_questions=len(
                questions
            ),

            candidate_name=candidate_name

        )


        # ==================================================
        # 9. Save Resume Data
        # ==================================================

        save_resume_data(

            db=db,

            session_id=session.id,

            parsed_data=parsed_data

        )


        # ==================================================
        # 10. Save Context
        # ==================================================

        save_context(

            db=db,

            session_id=session.id,

            context=context

        )


        # ==================================================
        # 11. Save Questions
        # ==================================================

        save_questions(

            db=db,

            session_id=session.id,

            questions=questions

        )


        # ==================================================
        # 12. Return Session
        # ==================================================

        return {

            "session_id": session.id,

            "role": target_role,

            "total_questions": len(
                questions
            )

        }


    finally:

        # ==================================================
        # 13. Delete Temporary Resume
        # ==================================================

        if os.path.exists(file_path):

            os.remove(file_path)
from uuid import UUID

from pydantic import BaseModel


# ==========================================================
# Candidate Entry Response
# ==========================================================

class CandidateEntryResponse(BaseModel):

    session_id: UUID

    role: str

    total_questions: int


# ==========================================================
# Question Response
# ==========================================================

class QuestionResponse(BaseModel):

    completed: bool

    session_id: UUID

    question_id: int | None = None

    question_number: int | None = None

    total_questions: int | None = None

    topic: str | None = None

    difficulty: str | None = None

    question_type: str | None = None

    question: str | None = None


# ==========================================================
# Answer Request
# ==========================================================

class AnswerRequest(BaseModel):

    session_id: UUID

    question_id: int

    answer: str


# ==========================================================
# Answer Response
# ==========================================================

class AnswerResponse(BaseModel):

    success: bool

    next_question: int | None = None

    completed: bool


# ==========================================================
# Interview Status
# ==========================================================

class InterviewStatusResponse(BaseModel):

    session_id: UUID

    candidate_name: str | None

    role: str

    status: str

    current_question: int

    total_questions: int

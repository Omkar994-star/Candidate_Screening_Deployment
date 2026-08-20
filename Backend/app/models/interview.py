import uuid

from app.core.database import Base

from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
    JSON
)

from sqlalchemy.dialects.postgresql import UUID,JSONB

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


# ==========================================================
# Base
# ==========================================================

class Base(DeclarativeBase):
    pass


# ==========================================================
# Interview Session
# ==========================================================

class InterviewSession(Base):

    __tablename__ = "interview_sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    candidate_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    target_role: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    resume_filename: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="in_progress",
        nullable=False
    )

    current_question: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    total_questions: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )


    # Relationships

    questions = relationship(
        "InterviewQuestion",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    answers = relationship(
        "InterviewAnswer",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    resume_data = relationship(
        "ResumeData",
        back_populates="session",
        uselist=False,
        cascade="all, delete-orphan"
    )

    context_data = relationship(
        "ContextData",
        back_populates="session",
        uselist=False,
        cascade="all, delete-orphan"
    )


# ==========================================================
# Interview Question
# ==========================================================

class InterviewQuestion(Base):

    __tablename__ = "interview_questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "interview_sessions.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    question_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    topic: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    difficulty: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    question_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    question: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    expected_skills: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True
    )


    session = relationship(
        "InterviewSession",
        back_populates="questions"
    )


# ==========================================================
# Interview Answer
# ==========================================================

class InterviewAnswer(Base):

    __tablename__ = "interview_answers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "interview_sessions.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey(
            "interview_questions.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    question_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    candidate_answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


    session = relationship(
        "InterviewSession",
        back_populates="answers"
    )


# ==========================================================
# Resume Data
# ==========================================================

class ResumeData(Base):

    __tablename__ = "resume_data"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "interview_sessions.id",
            ondelete="CASCADE"
        ),
        unique=True,
        nullable=False
    )

    parsed_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )


    session = relationship(
        "InterviewSession",
        back_populates="resume_data"
    )


# ==========================================================
# Context Data
# ==========================================================

class ContextData(Base):

    __tablename__ = "context_data"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "interview_sessions.id",
            ondelete="CASCADE"
        ),
        unique=True,
        nullable=False
    )

    context: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )


    session = relationship(
        "InterviewSession",
        back_populates="context_data"
    )


from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey
)








class InterviewEvaluation(Base):

    __tablename__ = "interview_evaluations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "interview_sessions.id"
        ),
        unique=True,
        nullable=False
    )

    overall_score = Column(
        Float,
        nullable=False
    )

    technical_score = Column(
        Float,
        nullable=False
    )

    problem_solving_score = Column(
        Float,
        nullable=False
    )

    communication_score = Column(
        Float,
        nullable=False
    )

    strengths = Column(
        JSONB,
        nullable=False,
        default=list
    )

    improvement_areas = Column(
        JSONB,
        nullable=False,
        default=list
    )

    summary = Column(
        Text,
        nullable=False
    )

    recommendation = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
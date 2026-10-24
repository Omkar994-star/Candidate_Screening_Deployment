import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ==========================================================
# Load environment variables
# ==========================================================

load_dotenv()


# ==========================================================
# PostgreSQL connection
# ==========================================================


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment")

# Use the installed psycopg2-binary driver
DATABASE_URL = DATABASE_URL.replace(
    "postgresql+psycopg://",
    "postgresql+psycopg2://",
    1
)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg2://",
        1
    )
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg2://",
        1
    )



if not DATABASE_URL:

    raise ValueError(
        "DATABASE_URL is not set in the .env file"
    )


# ==========================================================
# SQLAlchemy Engine
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# ==========================================================
# Base
#
# IMPORTANT:
# Every SQLAlchemy model must inherit from this Base.
# Alembic also uses this Base to discover models.
# ==========================================================

Base = declarative_base()


# ==========================================================
# Database Session
# ==========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================================
# FastAPI database dependency
# ==========================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
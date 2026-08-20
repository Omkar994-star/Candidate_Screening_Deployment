from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers.candidate import (
    router as candidate_router
)

from app.routers import evaluation


app = FastAPI(
    title="AI Candidate Screening API",
    version="1.0.0"
)


# ==========================================================
# CORS
# ==========================================================
#
# Allows the Next.js frontend to communicate with FastAPI.
#
# Frontend:
# http://localhost:3000
#
# Backend:
# http://127.0.0.1:8000
# ==========================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ==========================================================
# Routers
# ==========================================================

app.include_router(
    candidate_router
)

app.include_router(evaluation.router)


# ==========================================================
# Health Check
# ==========================================================

@app.get("/")
def health_check():

    return {
        "message":
            "AI Candidate Screening API is running"
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.candidate import router as candidate_router
from app.routers import evaluation


app = FastAPI(
    title="AI Candidate Screening API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        # Add your Vercel URL here later
        # "https://your-project.vercel.app"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(candidate_router)
app.include_router(evaluation.router)


@app.get("/")
def health_check():
    return {
        "message": "AI Candidate Screening API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
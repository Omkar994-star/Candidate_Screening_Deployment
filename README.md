## AI Candidate Screening

This is a resume-driven technical interview application. A candidate selects a supported job role, uploads a PDF or TXT resume, answers generated interview questions, and receives an AI-generated evaluation.

## Features

* Resume upload and text extraction for PDF and TXT files.
* Role-specific RAG retrieval from local FAISS vector databases.
* Gemini-powered resume parsing, interview-context construction, question generation, and final evaluation.
* Stateful interviews backed by PostgreSQL.
* Next.js candidate experience with question progress and evaluation results.
* Pre-generated role-specific FAISS indexes included in the repository.
* Server-side interview state that allows an interview to resume after a browser refresh.
* Idempotent evaluation generation to prevent duplicate evaluation records.

## System Architecture

```text
Browser (Next.js, :3000)
        |
        | HTTP / JSON / multipart upload
        v
FastAPI API (:8000)
  |-- Candidate router: roles, entry, questions, answers, status
  |-- Evaluation router: interview evaluation
  |
  |-- PostgreSQL
  |     interview sessions, questions, answers, parsed resumes,
  |     candidate context, and evaluation results
  |
  |-- Gemini API
  |     resume parsing -> context -> questions -> evaluation
  |
  `-- Local RAG
        Ollama embeddings + FAISS indexes in Backend/vector_db/
        sourced from Backend/rag/knowledge_base/
```

## Interview Flow

1. The frontend loads the roles whose FAISS indexes exist.
2. The candidate selects a supported role and submits a resume to `POST /candidate/entry`.
3. The backend extracts the resume text.
4. Gemini parses the resume into structured candidate information.
5. The backend builds the interview context.
6. Role-specific knowledge is retrieved from the local FAISS vector database.
7. Gemini generates the interview questions.
8. The generated questions and interview data are stored in PostgreSQL.
9. The frontend obtains and displays each question.
10. The candidate submits an answer for each question.
11. The backend saves each answer and advances the interview.
12. After the interview is completed, the evaluation endpoint generates or retrieves the evaluation.
13. The evaluation is stored in PostgreSQL and displayed on the frontend.

## Repository Layout

```text
AI_Candidate_Screening/
├── Backend/
│   ├── app/                         # FastAPI routes, services, database models, schemas
│   ├── alembic/                     # PostgreSQL schema migrations
│   ├── rag/                         # RAG pipeline and resume/interview processing
│   │   ├── knowledge_base/          # Role-specific knowledge-base documents
│   │   ├── __init__.py
│   │   ├── context_construction.py # Builds interview context from parsed resume data
│   │   ├── create_vector_db.py      # Creates role-specific FAISS vector databases
│   │   ├── knowledge_retrieve.py    # Retrieves relevant knowledge using FAISS
│   │   ├── llm_resume_parser.py     # Parses resumes using Gemini
│   │   ├── question_generator.py    # Generates interview questions
│   │   └── resume_text_extractor.py # Extracts text from PDF/TXT resumes
│   ├── vector_db/                   # Pre-generated role-specific FAISS indexes
│   │   └── <role>/
│   │       ├── index.faiss
│   │       └── index.pkl
│   ├── .env                         # Local environment variables; not committed
│   └── requirements.txt
│
└── frontend/
    ├── app/                         # Next.js App Router pages
    ├── components/                  # Resume, question, and result UI
    ├── lib/api.ts                   # Typed backend API client
    ├── .env.local                   # Optional frontend environment variables
    └── package.json
```

## Prerequisites

Install the following before setting up the project:

* Python 3.11 or later
* Node.js 20 or later
* PostgreSQL 14 or later
* Ollama
* A Google Gemini API key

The project uses Ollama locally for generating embeddings and Gemini for generative AI tasks.

## 1. Clone the Repository

Clone the project and open a terminal in the repository root:

```powershell
git clone <repository-url>
cd AI_Candidate_Screening
```

## 2. Configure the Backend

Open a terminal from the repository root:

```powershell
cd Backend
```

### Create the Python Virtual Environment

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the backend dependencies:

```powershell
pip install -r requirements.txt
```

## 3. Configure PostgreSQL

Install PostgreSQL if it is not already installed.

Create a PostgreSQL database named:

```text
candidate_screening_db
```

### Using pgAdmin

1. Open pgAdmin.
2. Connect to your PostgreSQL server.
3. Right-click `Databases`.
4. Select `Create` → `Database`.
5. Set the database name to `candidate_screening_db`.
6. Create the database.

### Using PostgreSQL

Alternatively, create the database from the PostgreSQL terminal:

```sql
CREATE DATABASE candidate_screening_db;
```

The PostgreSQL username and password used during installation will be required in the backend configuration.

## 4. Configure Backend Environment Variables

Create:

```text
Backend/.env
```

Add:

```dotenv
DATABASE_URL=postgresql+psycopg2://POSTGRES_USER:POSTGRES_PASSWORD@localhost:5432/pgagi3
GEMINI_API_KEY=your_gemini_api_key
```

Replace `POSTGRES_USER` and `POSTGRES_PASSWORD` with the PostgreSQL username and password configured on your system.

For example:

```dotenv
DATABASE_URL=postgresql+psycopg2://postgres:mypassword@localhost:5432/pgagi3
GEMINI_API_KEY=your_gemini_api_key
```

### Gemini API Key

Create your own Gemini API key and set it as:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
```

Do not commit the `.env` file or expose the Gemini API key in the repository.

## 5. Configure Ollama

Install Ollama and make sure it is available locally.

Pull the embedding model used by the RAG pipeline:

```powershell
ollama pull mxbai-embed-large
```

If Ollama is not already running, start it with:

```powershell
ollama serve
```

The application uses `mxbai-embed-large` for local document embeddings.

## 6. Apply Database Migrations

Make sure the PostgreSQL database `candidate_screening_db` exists and the backend virtual environment is activated.

From the `Backend` directory, run:

```powershell
alembic upgrade head
```

This creates the required PostgreSQL tables and database schema.

## 7. FAISS Vector Databases

The repository already contains the pre-generated role-specific FAISS vector databases under:

```text
Backend/vector_db/
```

For example:

```text
Backend/
└── vector_db/
    └── Python Developer/
        ├── index.faiss
        └── index.pkl
```

Therefore, **a new developer does not need to generate the vector database during normal project setup**.

The application discovers available roles from the directories inside:

```text
Backend/vector_db/
```

A role is available only when its corresponding valid FAISS index exists.

### Adding or Updating a Role

If the knowledge-base documents are modified or a new role is added in the future, the FAISS index can be regenerated.
For adding more roles in future, just add relevant documents in folder named same as role_name in the knowledge base and update the DirectoryLoader path and vector_db.save_local path in create_vector_db.py file and run this file manually.



This step is optional for normal setup because the required indexes are already included in the repository.

## 8. Start the Backend

From the `Backend` directory with the virtual environment activated:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The FastAPI API will run at:

```text
http://127.0.0.1:8000
```

The health endpoint is:

```text
http://127.0.0.1:8000/
```

FastAPI Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 9. Configure the Frontend

Open a **second terminal** from the repository root:

```powershell
cd frontend
```

Install the frontend dependencies:

```powershell
npm install
```

The frontend uses the backend at:

```text
http://127.0.0.1:8000
```

### Optional Frontend Environment Configuration

If the backend is running at another URL, create:

```text
frontend/.env.local
```

and add:

```dotenv
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## 10. Start the Frontend

From the `frontend` directory:

```powershell
npm run dev
```

The Next.js application will normally be available at:

```text
http://localhost:3000
```

Open the URL in a browser.

## API Overview

| Method | Endpoint                           | Purpose                                  |
| ------ | ---------------------------------- | ---------------------------------------- |
| `GET`  | `/`                                | API health check                         |
| `GET`  | `/candidate/roles`                 | List roles with an available FAISS index |
| `POST` | `/candidate/entry`                 | Upload a resume and create an interview  |
| `GET`  | `/candidate/{session_id}/question` | Get the active question                  |
| `POST` | `/candidate/answer`                | Save an answer and advance the interview |
| `GET`  | `/candidate/{session_id}/status`   | Restore interview state after refresh    |
| `POST` | `/candidate/{session_id}/evaluate` | Generate or retrieve the evaluation      |

## Key Design Decisions

### Role Availability Is Index-Driven

The backend derives selectable roles from directories in:

```text
Backend/vector_db/
```

that contain valid FAISS indexes.

This prevents the application from creating an interview for a role for which retrieval knowledge is unavailable.

Because the vector databases are included in the repository, supported roles are available immediately after cloning the project.

### Interview State Is Server-Side

Questions, answers, progress, parsed resume data, candidate context, and evaluations are persisted in PostgreSQL.

The browser stores only the interview session ID.

This allows the interview state to be restored after a browser refresh.

### Evaluations Are Idempotent

The evaluation service first checks whether an evaluation already exists for the interview session.

If one exists, it returns the existing evaluation.

Otherwise, it generates and stores a new evaluation.

This prevents duplicate evaluation records when the evaluation page is refreshed or the endpoint is called multiple times.

### Retrieval Stays Local; Generation Is Remote

The RAG pipeline uses:

```text
Ollama
    ↓
mxbai-embed-large
    ↓
FAISS
```

for local embedding and retrieval.

Gemini is used for generative tasks:

```text
Resume parsing
      ↓
Interview context construction
      ↓
Question generation
      ↓
Answer evaluation
```

### Explicit Frontend-Backend Contract

`frontend/lib/api.ts` contains the frontend request functions and response types used to communicate with the FastAPI backend.

The evaluation response is flat because the FastAPI evaluation endpoint returns the score and feedback fields at the top level.

## Environment Files

The project uses local environment files that should not be committed.

### Backend

```text
Backend/.env
```

Example:

```dotenv
DATABASE_URL=postgresql+psycopg2://postgres:mypassword@localhost:5432/pgagi3
GEMINI_API_KEY=your_gemini_api_key
```

### Frontend

```text
frontend/.env.local
```

Example:

```dotenv
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

The frontend `.env.local` file is optional when using the default backend URL.

## Complete Setup Summary

For a new developer, the complete setup is:

```powershell
# 1. Clone
git clone <repository-url>
cd AI_Candidate_Screening

# 2. Create PostgreSQL database
# Database name: candidate_screening_db

# 3. Backend
cd Backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 4. Configure Backend/.env
# DATABASE_URL=...
# GEMINI_API_KEY=...

# 5. Configure Ollama
ollama pull mxbai-embed-large

# 6. Apply database migrations
alembic upgrade head

# 7. Start backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open a second terminal:

```powershell
# 8. Frontend
cd frontend
npm install

# 9. Start frontend
npm run dev
```

Then open:

```text
http://localhost:3000
```

**No FAISS generation step is required for the included roles because `Backend/vector_db/` is already included in the repository.**

## Validation Commands

### Frontend Production Build

```powershell
cd frontend
npm run build
```

### Backend Syntax Check

```powershell
cd ..\Backend
.\venv\Scripts\python.exe -m compileall -q app rag alembic
```

## Troubleshooting

### Backend Cannot Connect to PostgreSQL

Check that:

* PostgreSQL is running.
* The `candidate_screening_db` database exists.
* The username in `DATABASE_URL` is correct.
* The password in `DATABASE_URL` is correct.
* The PostgreSQL port is correct, normally `5432`.

### No Roles Appear in the Frontend

Check:

```text
Backend/vector_db/
```

and make sure the expected role directory and FAISS files exist.

For example:

```text
Backend/vector_db/Python Developer/
├── index.faiss
└── index.pkl
```

### Ollama Connection Error

Make sure Ollama is installed and running:

```powershell
ollama serve
```

Also verify that the embedding model has been downloaded:

```powershell
ollama list
```

The following model should be present:

```text
mxbai-embed-large
```

### Gemini API Error

Check that:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
```

is correctly configured in:

```text
Backend/.env
```

Also make sure the API key is valid and has available quota.

### Frontend Cannot Reach Backend

Make sure FastAPI is running on:

```text
http://127.0.0.1:8000
```

If using a different backend URL, update:

```text
frontend/.env.local
```

with:

```dotenv
NEXT_PUBLIC_API_URL=<your-backend-url>
```

Then restart the Next.js development server.

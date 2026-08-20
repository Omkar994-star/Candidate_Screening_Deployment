const API_URL =
  process.env.NEXT_PUBLIC_API_URL ||
  "http://127.0.0.1:8000";


// ==========================================================
// Types
// ==========================================================

export interface CandidateEntryResponse {
  session_id: string;
  role: string;
  total_questions: number;
}


export interface RecruitmentRolesResponse {
  roles: string[];
}


export interface QuestionResponse {
  completed: boolean;
  session_id: string;

  question_id?: number;
  question_number?: number;
  total_questions?: number;

  topic?: string;
  difficulty?: string;
  question_type?: string;

  question?: string;
}


export interface AnswerResponse {
  success: boolean;
  next_question?: number | null;
  completed: boolean;
}


// ==========================================================
// Start Interview
// ==========================================================

export async function startInterview(
  file: File,
  role: string
): Promise<CandidateEntryResponse> {

  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  formData.append("role", role);


  // ========================================================
  // BACKEND CONNECTION
  //
  // POST /candidate/entry
  //
  // The resume and selected recruitment role are sent together.
  // ========================================================

  const response = await fetch(

    `${API_URL}/candidate/entry`,

    {
      method: "POST",

      body: formData
    }

  );


  if (!response.ok) {

    const error =
      await response.json()
        .catch(() => null);


    throw new Error(

      error?.detail ||
      "Failed to start interview"

    );

  }


  return response.json();
}


export async function getRecruitmentRoles(): Promise<string[]> {
  const response = await fetch(`${API_URL}/candidate/roles`, {
    method: "GET",
    cache: "no-store"
  });

  if (!response.ok) {
    const error = await response.json().catch(() => null);
    throw new Error(error?.detail || "Failed to load recruitment roles");
  }

  const data: RecruitmentRolesResponse = await response.json();
  return data.roles;
}


// ==========================================================
// Get Current Question
// ==========================================================

export async function getCurrentQuestion(
  sessionId: string
): Promise<QuestionResponse> {

  // ========================================================
  // BACKEND CONNECTION
  //
  // GET /candidate/{session_id}/question
  //
  // This returns ONLY the current question.
  // ========================================================

  const response = await fetch(
    `${API_URL}/candidate/${sessionId}/question`,
    {
      method: "GET",
      cache: "no-store"
    }
  );


  if (!response.ok) {

    const error = await response.json()
      .catch(() => null);

    throw new Error(
      error?.detail ||
      "Failed to load question"
    );
  }


  return response.json();
}


// ==========================================================
// Submit Answer
// ==========================================================

export async function submitAnswer(
  sessionId: string,
  questionId: number,
  answer: string
): Promise<AnswerResponse> {

  // ========================================================
  // BACKEND CONNECTION
  //
  // POST /candidate/answer
  //
  // After saving the answer, the backend automatically
  // moves current_question to the next question.
  // ========================================================

  const response = await fetch(
    `${API_URL}/candidate/answer`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({

        session_id: sessionId,

        question_id: questionId,

        answer: answer

      })
    }
  );


  if (!response.ok) {

    const error = await response.json()
      .catch(() => null);

    throw new Error(
      error?.detail ||
      "Failed to submit answer"
    );
  }


  return response.json();
}


export interface InterviewStatusResponse {

  session_id: string;

  candidate_name: string | null;

  role: string;

  status: string;

  current_question: number;

  total_questions: number;

}





export async function getInterviewStatus(
  sessionId: string
): Promise<InterviewStatusResponse> {

  // ========================================================
  // BACKEND CONNECTION
  //
  // GET /candidate/{session_id}/status
  //
  // Used to restore the interview state after a browser
  // refresh.
  // ========================================================

  const response = await fetch(

    `${API_URL}/candidate/${sessionId}/status`,

    {
      method: "GET",

      cache: "no-store"
    }

  );


  if (!response.ok) {

    const error =
      await response.json()
        .catch(() => null);


    throw new Error(

      error?.detail ||
      "Failed to load interview status"

    );

  }


  return response.json();
}



export interface EvaluationResponse {
  id: number;
  session_id: string;
  overall_score: number;
  technical_score: number;
  problem_solving_score: number;
  communication_score: number;
  strengths: string[];
  improvement_areas: string[];
  summary: string;
  recommendation: string;
  created_at: string | null;
}


export async function evaluateInterview(
  sessionId: string
): Promise<EvaluationResponse> {

  // ======================================================
  // BACKEND CONNECTION
  //
  // POST /candidate/{session_id}/evaluate
  //
  // Backend fetches all stored questions and answers,
  // sends them to the evaluation LLM and stores the
  // resulting evaluation in PostgreSQL.
  // ======================================================

  const response = await fetch(

    `${API_URL}/candidate/${sessionId}/evaluate`,

    {
      method: "POST"
    }

  );


  if (!response.ok) {

    const error =
      await response.json()
        .catch(() => null);


    throw new Error(

      error?.detail ||
      "Failed to generate evaluation"

    );

  }


  return response.json();
}



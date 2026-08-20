"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import InterviewQuestion from "@/components/InterviewQuestion";

import {
  getInterviewStatus,
  getCurrentQuestion,
  submitAnswer,
  QuestionResponse,
} from "@/lib/api";


export default function InterviewPage() {

  const router = useRouter();

  // ========================================================
  // SESSION ID
  // ========================================================

  const [sessionId, setSessionId] =
    useState<string | null>(null);


  // ========================================================
  // RECRUITER DEFINED ROLE
  // ========================================================

  const [role, setRole] =
    useState("");


  // ========================================================
  // CURRENT QUESTION
  // ========================================================

  const [question, setQuestion] =
    useState<QuestionResponse | null>(null);


  // ========================================================
  // LOADING
  // ========================================================

  const [loading, setLoading] =
    useState(true);


  // ========================================================
  // ANSWER SUBMITTING
  // ========================================================

  const [submitting, setSubmitting] =
    useState(false);


  // ========================================================
  // ERROR
  // ========================================================

  const [error, setError] =
    useState("");


  // ========================================================
  // INTERVIEW COMPLETED
  // ========================================================

  const [completed, setCompleted] =
    useState(false);


  // ========================================================
  // LOAD SESSION
  // ========================================================

  useEffect(() => {

    const storedSessionId =
      sessionStorage.getItem("session_id");


    if (!storedSessionId) {

      router.push("/");

      return;

    }


    setSessionId(
      storedSessionId
    );


    restoreInterview(
      storedSessionId
    );

  }, [router]);


  // ========================================================
  // RESTORE INTERVIEW
  // ========================================================

  async function restoreInterview(
    id: string
  ) {

    try {

      setLoading(true);
      setError("");


      // ====================================================
      // BACKEND CONNECTION
      //
      // GET /candidate/{session_id}/status
      //
      // Gets the recruiter-defined role and interview status.
      // ====================================================

      const status =
        await getInterviewStatus(id);


      setRole(
        status.role
      );


      // ====================================================
      // IF ALREADY COMPLETED
      //
      // Show completed page.
      //
      // Evaluation is handled separately.
      // ====================================================

      if (
        status.status === "completed"
      ) {

        setCompleted(true);

        return;

      }


      // ====================================================
      // LOAD CURRENT QUESTION
      // ====================================================

      await loadQuestion(id);

    } catch (error) {

      console.error(
        "Failed to restore interview:",
        error
      );


      setError(

        error instanceof Error
          ? error.message
          : "Unable to restore interview."

      );

    } finally {

      setLoading(false);

    }

  }


  // ========================================================
  // LOAD CURRENT QUESTION
  // ========================================================

  async function loadQuestion(
    id: string
  ) {

    try {

      setLoading(true);
      setError("");


      // ====================================================
      // BACKEND CONNECTION
      //
      // GET /candidate/{session_id}/question
      // ====================================================

      const result =
        await getCurrentQuestion(id);


      // ====================================================
      // NO MORE QUESTIONS
      // ====================================================

      if (result.completed) {

        setQuestion(null);

        setCompleted(true);

        return;

      }


      // ====================================================
      // DISPLAY QUESTION
      // ====================================================

      setQuestion(result);

    } catch (error) {

      console.error(
        "Failed to load question:",
        error
      );


      setError(

        error instanceof Error
          ? error.message
          : "Failed to load question."

      );

    } finally {

      setLoading(false);

    }

  }


  // ========================================================
  // SUBMIT ANSWER
  // ========================================================

  async function handleAnswer(
    answer: string
  ) {

    if (!sessionId) {
      return;
    }


    if (!question?.question_id) {
      return;
    }


    try {

      setSubmitting(true);
      setError("");


      // ====================================================
      // BACKEND CONNECTION
      //
      // POST /candidate/answer
      //
      // Backend:
      //
      // 1. Saves candidate answer
      // 2. Determines next question
      // 3. Returns completed=true for final question
      // ====================================================

      const result =
        await submitAnswer(

          sessionId,

          question.question_id,

          answer

        );


      // ====================================================
      // FINAL QUESTION
      // ====================================================

      if (result.completed) {

        setQuestion(null);

        setCompleted(true);

        return;

      }


      // ====================================================
      // NEXT QUESTION
      //
      // There is intentionally NO previous-question option.
      // ====================================================

      await loadQuestion(
        sessionId
      );

    } catch (error) {

      console.error(
        "Failed to submit answer:",
        error
      );


      setError(

        error instanceof Error
          ? error.message
          : "Failed to submit answer."

      );

    } finally {

      setSubmitting(false);

    }

  }


  // ========================================================
  // LOADING SCREEN
  // ========================================================

  if (loading) {

    return (

      <main className="center-page">

        <div className="loading">

          Preparing your interview...

        </div>

      </main>

    );

  }


  // ========================================================
  // INTERVIEW COMPLETED SCREEN
  // ========================================================
  //
  // IMPORTANT:
  //
  // Evaluation is NOT generated here.
  //
  // Candidate explicitly clicks:
  //
  // "View Evaluation Result"
  //
  // ========================================================

  if (completed) {

    return (

      <main className="center-page">

        <div className="completion-card">

          <h1>
            Interview Completed
          </h1>


          <p>
            Thank you for completing the interview.
          </p>


          <p>
            Your responses have been submitted
            successfully.
          </p>


          <button
            className="primary-button"
            onClick={() => {

              // ==========================================
              // Store session ID again so the evaluation
              // page can retrieve the correct interview.
              // ==========================================

              if (sessionId) {

                sessionStorage.setItem(
                  "session_id",
                  sessionId
                );

              }


              // ==========================================
              // Go to separate evaluation page.
              // ==========================================

              router.push(
                "/evaluation"
              );

            }}
          >

            View Evaluation Result

          </button>

        </div>

      </main>

    );

  }


  // ========================================================
  // ERROR SCREEN
  // ========================================================

  if (error && !question) {

    return (

      <main className="center-page">

        <div className="error-card">

          <h2>
            Something went wrong
          </h2>


          <p>
            {error}
          </p>


          <button
            className="primary-button"
            onClick={() =>
              router.push("/")
            }
          >

            Back

          </button>

        </div>

      </main>

    );

  }


  // ========================================================
  // INTERVIEW UI
  // ========================================================

  return (

    <main className="interview-page">


      {/* ==================================================
          HEADER
          ================================================== */}

      <header className="interview-header">

        <div>

          <h1>
            Technical Interview
          </h1>


          <p>

            Role:{" "}

            <strong>
              {role}
            </strong>

          </p>

        </div>

      </header>


      {/* ==================================================
          ERROR MESSAGE
          ================================================== */}

      {error && (

        <div className="error-message">

          {error}

        </div>

      )}


      {/* ==================================================
          QUESTION
          ================================================== */}

      {question && (

        <InterviewQuestion

          question={question}

          onSubmit={handleAnswer}

          submitting={submitting}

        />

      )}

    </main>

  );

}
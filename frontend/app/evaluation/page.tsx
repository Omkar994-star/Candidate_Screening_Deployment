"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import {
  evaluateInterview,
  EvaluationResponse,
} from "@/lib/api";

import InterviewResult from "@/components/InterviewResult";


export default function EvaluationPage() {

  const router = useRouter();

  const [evaluation, setEvaluation] =
    useState<EvaluationResponse | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");


  // ========================================================
  // Load Evaluation
  // ========================================================

  useEffect(() => {

    const sessionId =
      sessionStorage.getItem("session_id");

    if (!sessionId) {

      router.push("/");

      return;

    }

    loadEvaluation(sessionId);

  }, [router]);


  // ========================================================
  // Load Evaluation From Backend
  // ========================================================

  async function loadEvaluation(
    sessionId: string
  ) {

    try {

      setLoading(true);

      setError("");


      // ====================================================
      // BACKEND CONNECTION
      //
      // POST /candidate/{session_id}/evaluate
      //
      // Backend returns the saved/generated evaluation.
      // ====================================================

      const result =
        await evaluateInterview(sessionId);


      setEvaluation(result);

    }

    catch (error) {

      console.error(
        "Failed to load evaluation:",
        error
      );

      setError(

        error instanceof Error
          ? error.message
          : "Failed to load evaluation."

      );

    }

    finally {

      setLoading(false);

    }

  }


  // ========================================================
  // Loading UI
  // ========================================================

  if (loading) {

    return (

      <main className="evaluation-page">

        <div className="evaluation-loading">

          <div className="loading-spinner"></div>

          <h1>
            Preparing Your Evaluation
          </h1>

          <p>
            We are analyzing your interview responses.
          </p>

          <span>
            This may take a few moments...
          </span>

        </div>

      </main>

    );

  }


  // ========================================================
  // Error UI
  // ========================================================

  if (error) {

    return (

      <main className="evaluation-page">

        <div className="evaluation-error">

          <div className="error-icon">
            !
          </div>

          <h1>
            Unable to Load Evaluation
          </h1>

          <p>
            {error}
          </p>

          <button
            className="evaluation-button"
            onClick={() =>
              router.push("/interview")
            }
          >
            Back to Interview
          </button>

        </div>

      </main>

    );

  }


  // ========================================================
  // Evaluation Result
  // ========================================================

  if (evaluation) {

    return (

      <main className="evaluation-page">

        <div className="evaluation-container">

          {/* ==================================================
              Header
          ================================================== */}

          <header className="evaluation-header">

            <div>

              <span className="evaluation-label">
                INTERVIEW RESULTS
              </span>

              <h1>
                Interview Evaluation
              </h1>

              <p>
                Here is a summary of your interview performance.
              </p>

            </div>

          </header>


          {/* ==================================================
              Existing Interview Result Component
              
              Your InterviewResult component is responsible
              for displaying the actual evaluation data.
          ================================================== */}

          <section className="evaluation-result-wrapper">

            <InterviewResult
              result={evaluation}
            />

          </section>


          {/* ==================================================
              Bottom Action
          ================================================== */}

          <div className="evaluation-footer">

            <p>
              Thank you for completing the interview.
            </p>

            <button
              className="evaluation-button"
              onClick={() =>
                router.push("/")
              }
            >
              Finish
            </button>

          </div>

        </div>

      </main>

    );

  }


  return null;

}

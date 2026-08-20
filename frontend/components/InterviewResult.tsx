"use client";

import { EvaluationResponse } from "@/lib/api";

interface InterviewResultProps {
  result: EvaluationResponse;
}


export default function InterviewResult({
  result
}: InterviewResultProps) {

  // ========================================================
  // Safety check
  // ========================================================

  if (!result) {

    return (

      <main className="center-page">

        <div className="error-card">

          <h2>
            Evaluation not available
          </h2>

          <p>
            We could not load the interview evaluation.
          </p>

        </div>

      </main>

    );

  }


  // ========================================================
  // Render Evaluation
  // ========================================================

  return (

    <main className="evaluation-page">

      <div className="evaluation-container">


        {/* ==================================================
            Header
        ================================================== */}

        <div className="evaluation-header">

          <h1>
            Interview Evaluation
          </h1>

          <p>
            Your interview evaluation is ready.
          </p>

        </div>


        {/* ==================================================
            Overall Score
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Overall Score
          </h2>


          <div className="overall-score-container">

            <strong className="overall-score">

              {result.overall_score}

              <span>/100</span>

            </strong>

          </div>

        </section>


        {/* ==================================================
            Score Breakdown
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Score Breakdown
          </h2>


          <div className="score-grid">


            {/* Technical */}

            <div className="score-item">

              <span>
                Technical
              </span>

              <strong>
                {result.technical_score}/100
              </strong>

            </div>


            {/* Problem Solving */}

            <div className="score-item">

              <span>
                Problem Solving
              </span>

              <strong>
                {result.problem_solving_score}/100
              </strong>

            </div>


            {/* Communication */}

            <div className="score-item">

              <span>
                Communication
              </span>

              <strong>
                {result.communication_score}/100
              </strong>

            </div>


          </div>

        </section>


        {/* ==================================================
            Strengths
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Strengths
          </h2>


          {result.strengths &&
          result.strengths.length > 0 ? (

            <ul>

              {result.strengths.map(
                (
                  strength,
                  index
                ) => (

                  <li key={index}>

                    {strength}

                  </li>

                )
              )}

            </ul>

          ) : (

            <p>
              No specific strengths were identified.
            </p>

          )}

        </section>


        {/* ==================================================
            Improvement Areas
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Areas for Improvement
          </h2>


          {result.improvement_areas &&
          result.improvement_areas.length > 0 ? (

            <ul>

              {result.improvement_areas.map(
                (
                  area,
                  index
                ) => (

                  <li key={index}>

                    {area}

                  </li>

                )
              )}

            </ul>

          ) : (

            <p>
              No specific improvement areas were identified.
            </p>

          )}

        </section>


        {/* ==================================================
            Summary
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Summary
          </h2>


          <p className="evaluation-summary">

            {result.summary}

          </p>

        </section>


        {/* ==================================================
            Recommendation
        ================================================== */}

        <section className="evaluation-card">

          <h2>
            Recommendation
          </h2>


          <p className="recommendation">

            {result.recommendation}

          </p>

        </section>


      </div>

    </main>

  );

}

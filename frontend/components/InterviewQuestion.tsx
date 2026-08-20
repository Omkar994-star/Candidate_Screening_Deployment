"use client";

import { useState } from "react";

import {
  QuestionResponse
} from "@/lib/api";


interface Props {

  question: QuestionResponse;

  onSubmit: (
    answer: string
  ) => Promise<void>;

  submitting: boolean;

}


export default function InterviewQuestion({

  question,

  onSubmit,

  submitting

}: Props) {


  const [answer, setAnswer] =
    useState("");


  // ========================================================
  // Submit Answer
  // ========================================================

  async function handleSubmit() {

    if (!answer.trim()) {

      return;

    }


    await onSubmit(
      answer.trim()
    );

  }


  return (

    <div className="question-card">


      {/* ====================================================
          Progress
          ==================================================== */}

      <div className="question-progress">

        Question{" "}

        {question.question_number}

        {" "}of{" "}

        {question.total_questions}

      </div>


      {/* ====================================================
          Topic / Difficulty
          ==================================================== */}

      <div className="question-meta">

        {question.topic && (

          <span>
            {question.topic}
          </span>

        )}


        {question.difficulty && (

          <span>
            {question.difficulty}
          </span>

        )}

      </div>


      {/* ====================================================
          Question
          ==================================================== */}

      <h2 className="question-text">

        {question.question}

      </h2>


      {/* ====================================================
          Answer
          ==================================================== */}

      <textarea

        value={answer}

        onChange={(event) =>
          setAnswer(event.target.value)
        }

        placeholder="Type your answer here..."

        rows={8}

        disabled={submitting}

      />


      {/* ====================================================
          Submit / Next
          ==================================================== */}

      <button

        className="primary-button"

        onClick={handleSubmit}

        disabled={
          submitting ||
          !answer.trim()
        }

      >

        {submitting
          ? "Saving..."
          : "Next"
        }

      </button>


    </div>

  );

}
"use client";

import { useEffect, useState } from "react";

import {
  startInterview,
  getRecruitmentRoles
} from "@/lib/api";

import {
  useRouter
} from "next/navigation";




export default function ResumeUpload() {

  const router = useRouter();

  const [role, setRole] =
    useState("");

  const [roles, setRoles] =
    useState<string[]>([]);


  const [file, setFile] =
    useState<File | null>(null);


  const [loading, setLoading] =
    useState(false);


  const [error, setError] =
    useState("");

  useEffect(() => {
  async function loadRole() {
    try {
      const availableRoles =
        await getRecruitmentRoles();

      setRoles(availableRoles);

    } catch (error) {
      setError(
        error instanceof Error
          ? error.message
          : "Failed to load recruitment role."
      );
    }
  }

  loadRole();
}, []);


  // ========================================================
  // File Selection
  // ========================================================

  function handleFileChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {

    const selectedFile =
      event.target.files?.[0];


    if (!selectedFile) {
      return;
    }


    // Only allow PDF and TXT

    const allowedTypes = [
      "application/pdf",
      "text/plain"
    ];


    if (!allowedTypes.includes(
      selectedFile.type
    )) {

      setError(
        "Please upload a PDF or TXT resume."
      );

      setFile(null);

      return;
    }


    setError("");

    setFile(selectedFile);
  }


  // ========================================================
  // Start Interview
  // ========================================================

  async function handleStartInterview() {

    if (!file) {

      setError(
        "Please upload your resume first."
      );

      return;
    }


    try {

      setLoading(true);

      setError("");


      // ====================================================
      // BACKEND CONNECTION
      //
      // Sends the resume to:
      //
      // POST /candidate/entry
      //
      // Backend:
      // Resume → Gemini → RAG → Questions → PostgreSQL
      // ====================================================

      if (!role) {
        setError("Please select a recruitment role.");
        return;
      }

      const result =
        await startInterview(file, role);


      // Save session ID temporarily.
      //
      // The interview page will use this ID for:
      //
      // GET question
      // POST answer
      // POST submit

      sessionStorage.setItem(
        "session_id",
        result.session_id
      );


      


      // Go to interview screen

      router.push("/interview");

    } catch (error) {

      setError(
        error instanceof Error && error.message !== "Failed to fetch"
          ? error.message
          : "Unable to connect to the interview server. Please try again."
      );

    } finally {

      setLoading(false);

    }
  }


  return (

    <div className="upload-container">

      <div className="upload-card">

        <h1>
          Candidate Screening
        </h1>


        <p className="subtitle">
          Technical interview screening
        </p>


        <div className="role-section">

          <label>
            Select Job Role 
          </label>

          <select
            className="role-box"
            value={role}
            onChange={(event) => setRole(event.target.value)}
            disabled={loading || roles.length === 0}
          >
            <option value="" disabled>
              Job Roles
            </option>
            {roles.map((availableRole) => (
              <option key={availableRole} value={availableRole}>
                {availableRole}
              </option>
            ))}
          </select>

        </div>


        {/* ==================================================
            Resume Upload
            ================================================== */}

        <div className="upload-section">

          <label>
            Upload Resume
          </label>


          <input
            type="file"
            accept=".pdf,.txt"
            onChange={handleFileChange}
          />


          {file && (

            <p className="file-name">
              Selected: {file.name}
            </p>

          )}

        </div>


        {/* ==================================================
            Error
            ================================================== */}

        {error && (

          <div className="error-message">
            {error}
          </div>

        )}


        {/* ==================================================
            Start Button
            ================================================== */}

        <button
          className="primary-button"
          onClick={handleStartInterview}
          disabled={loading}
        >

          {loading
            ? "Preparing Interview..."
            : "Start Interview"
          }

        </button>

      </div>

    </div>

  );
}
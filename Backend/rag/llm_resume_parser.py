import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def parse_resume_with_llm(resume_text: str):

    """
    Parse resume text using Gemini and return structured JSON.
    """

    prompt = f"""
You are an expert Resume Parser.

Analyze the given resume and extract only the information that is explicitly mentioned or can be reasonably inferred.

Rules:
1. Return ONLY valid JSON.
2. Do NOT include markdown.
3. Do NOT wrap the response in ```json.
4. Do NOT add explanations.
5. Do NOT invent information.
6. If a field is unavailable:
   - Use "" for strings.
   - Use [] for arrays.
   - Use 0 for numeric values.

JSON Schema:

{{
    "candidate_name": "",

    "email_id": "",

    Contact Number": "",

    "skills": [],

    "technologies": [],

    "frameworks": [],

    "programming_languages": [],

    "tools": [],

    "databases": [],

    "cloud_platforms": [],

    "domain_exposure": [],

    "projects": [
        {{
            "title": "",
            "description": "",
            "technologies": [],
            "domain": ""
        }}
    ],

    "experience_level": "",

    "years_of_experience": 0,

    "education": [
        {{
            "degree": "",
            "specialization": "",
            "institution": "",
            "completion_year": ""
        }}
    ],

    "certifications": [],
    "recommended_role": ""
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
    )

    response_text = response.text.strip()

    # Remove markdown code fences if present
    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)
        response_text = response_text.rsplit("```", 1)[0].strip()
    elif response_text.startswith("```"):
        response_text = response_text.replace("```", "", 1)
        response_text = response_text.rsplit("```", 1)[0].strip()

    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Gemini returned invalid JSON:\n\n{response_text}"
        ) from e
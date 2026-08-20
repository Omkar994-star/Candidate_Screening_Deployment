import os
import json
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def build_context(target_role: str, resume_data: dict):

    prompt = f"""
You are an expert technical interviewer.

Candidate Target Role:
{target_role}

Candidate Resume Data:
{json.dumps(resume_data, indent=2)}

Your task is to construct the interview context.

Instructions:

1. Analyze the target role and candidate's resume.
2. Identify the core technical topics that should be evaluated considering target role.
3. Identify the relevant domains or knowledge areas.
4. Generate meaningful search queries that can be used to retrieve:
   - technical concepts
   - interview questions
   - coding problems
   - best practices
   - scenario-based questions
5. Generate queries that combine both the target role and the relevant candidate's experience.

Return ONLY valid JSON.

Schema:

{{
    "evaluation_topics": [],
    "domains": [],
    "search_queries": [],
    "difficulty_level": "",
    "priority_topics": []
}}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    response_text = response.text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)
        response_text = response_text.rsplit("```", 1)[0].strip()

    return json.loads(response_text)



import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_questions(context, knowledge,parsed_data,target_role):

    knowledge_text = "\n\n".join(
        doc.page_content for doc in knowledge
    )

    prompt = f"""
You are an expert technical interviewer.

target_role: {target_role}

Resume Data:
{json.dumps(parsed_data, indent=2)}

Candidate Context:
{json.dumps(context, indent=2)}

Retrieved Knowledge:
{knowledge_text}

Generate 10 interview questions based ONLY on the retrieved knowledge and candidate context.

Instructions:
1. Return ONLY valid JSON.
2. No markdown.
3. Cover all important topics.
4. Only 20% questions on relevent candidate context and resume data with respect to role, 10% on exact role and 70% on retrieved knowledge.
5. Give a mix of conceptual, coding, debugging, scenario and follow-up questions.
6. Difficulty level should match the specified target role.


Schema:

{{
  "questions":[
    {{
      "id":1,
      "topic":"",
      "difficulty":"",
      "type":"",
      "question":"",
      "expected_skills":[]
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)
        text = text.rsplit("```", 1)[0].strip()

    return json.loads(text)
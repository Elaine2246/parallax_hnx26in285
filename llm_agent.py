
import json
import os

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

client = genai.Client(api_key=api_key)


def generate_analysis(question, schema):
    prompt = f"""
{SYSTEM_PROMPT}

Available data schema:
{json.dumps(schema, indent=2)}

User question:
{question}

Return only a valid JSON object with these keys:
status, plan, code, assumptions, message.
"""

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "temperature": 0
        }
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    answer = json.loads(response.text)
    return validate_response(answer)

def validate_response(answer):
    required_keys = {
        "status",
        "plan",
        "code",
        "assumptions",
        "message"
    }

    if not isinstance(answer, dict):
        raise ValueError("AI response must be a JSON object.")

    missing = required_keys - answer.keys()
    if missing:
        raise ValueError(f"Missing fields: {missing}")

    if answer["status"] not in {
        "ready",
        "clarification_needed",
        "cannot_answer"
    }:
        raise ValueError("Invalid status returned by AI.")

    if not isinstance(answer["plan"], list):
        raise ValueError("Plan must be a list.")

    if not isinstance(answer["assumptions"], list):
        raise ValueError("Assumptions must be a list.")

    if not isinstance(answer["code"], str):
        raise ValueError("Code must be a string.")

    if not isinstance(answer["message"], str):
        raise ValueError("Message must be a string.")

    if answer["status"] == "ready" and not answer["code"].strip():
        raise ValueError("Ready response must contain proposed code.")

    return answer

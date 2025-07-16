import os
import time
import requests
from dotenv import load_dotenv
from preference_store import get_preferences

load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")

def get_agent_response(message, name="default"):
    if not API_KEY:
        raise ValueError("GROQ_API_KEY not set in environment variables.")

    preferences = get_preferences(name)
    if preferences:
        prompt = (
            "You are a scheduling assistant. Based on the user's preferences, "
            "propose ideal meeting times and ask for confirmation if needed.\n\n"
            f"User preferences:\n"
            f"- Name: {name}\n"
            f"- Email: {preferences.get('email')}\n"
            f"- Calendar type: {preferences.get('calendar_type')}\n"
            f"- Available days: {preferences.get('available_days', [])}\n"
            f"- Time range: {preferences.get('time_range', 'N/A')}\n"
            f"- Duration: {preferences.get('duration', 'N/A')} minutes\n\n"
            f"User input: {message}"
        )
    else:
        prompt = f"User has not set preferences. Please assist with this request: {message}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    for attempt in range(2):  # Retry once on failure
        try:
            response = requests.post(API_URL, headers=headers, json=body, timeout=10)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.HTTPError as e:
            if response.status_code >= 500 and attempt == 0:
                time.sleep(1)
                continue
            return f"Something went wrong: {str(e)}"
        except Exception as e:
            print("Prompt that caused failure:", prompt)
            return f"Unexpected error: {str(e)}"

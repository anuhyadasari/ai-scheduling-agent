from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import get_agent_response
from preference_store import save_preferences_for_user, get_preferences
from google_calendar import create_google_event
from outlook_email import send_outlook_invite

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class QueryRequest(BaseModel):
    user_input: str
    name: str = "default"

class PreferenceRequest(BaseModel):
    name: str
    email: str
    calendar_type: str  # google or outlook
    available_days: list[str]
    time_range: str
    duration: int

class ScheduleRequest(BaseModel):
    name: str
    day: str
    time: str
    topic: str

@app.post("/ask/")
async def ask_agent(request: QueryRequest):
    try:
        response = get_agent_response(request.user_input, request.name)
        return {"response": response}
    except Exception as e:
        return {"response": f"Something went wrong: {str(e)}"}

@app.post("/preferences/")
async def save_preferences(pref: PreferenceRequest):
    save_preferences_for_user(pref.name, {
        "email": pref.email,
        "calendar_type": pref.calendar_type,
        "available_days": pref.available_days,
        "time_range": pref.time_range,
        "duration": pref.duration,
    })
    return {"message": "Preferences saved"}

@app.post("/schedule/")
async def schedule_meeting(req: ScheduleRequest):
    prefs = get_preferences(req.name)
    if not prefs:
        return {"message": "No preferences found"}

    email = prefs["email"]
    calendar_type = prefs["calendar_type"]

    if calendar_type == "google":
        event = create_google_event(email, req.day, req.time, prefs["duration"], req.topic)
        return {"message": f"Google Calendar invite created: {event}"}
    elif calendar_type == "outlook":
        send_outlook_invite(email, req.day, req.time, prefs["duration"], req.topic)
        return {"message": "Outlook invite sent"}
    else:
        return {"message": "Unsupported calendar type"}

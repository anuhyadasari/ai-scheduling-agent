from datetime import datetime, timedelta

def suggest_meeting_times(query: str = "") -> str:
    now = datetime.now()
    slot1 = (now + timedelta(hours=1)).strftime("%A %I:%M %p")
    slot2 = (now + timedelta(hours=2)).strftime("%A %I:%M %p")
    slot3 = (now + timedelta(hours=3)).strftime("%A %I:%M %p")
    return f"Suggested slots: {slot1}, {slot2}, {slot3}"

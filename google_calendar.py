from datetime import datetime, timedelta

def create_google_event(email, day, time, duration, topic):
    start_dt = datetime.strptime(f"{day} {time}", "%A %I%p")
    end_dt = start_dt + timedelta(minutes=duration)
    return f"Google event scheduled for {email} on {day} at {time} about '{topic}' ({start_dt.strftime('%I:%M %p')} - {end_dt.strftime('%I:%M %p')})"

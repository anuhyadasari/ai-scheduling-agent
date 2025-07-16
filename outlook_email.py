import smtplib
from email.message import EmailMessage
import os

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.office365.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))

def send_outlook_invite(to_email, day, time, duration, topic):
    msg = EmailMessage()
    msg["Subject"] = f"Meeting: {topic}"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg.set_content(f"Scheduled meeting on {day} at {time} for {duration} mins. Topic: {topic}")

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

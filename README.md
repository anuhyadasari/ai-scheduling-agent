# AI Scheduling Agent – Backend

This is the backend for the AI-powered scheduling assistant. It handles user preferences, generates intelligent scheduling suggestions using LLMs (Groq), integrates with Google Calendar and Outlook, and manages meeting workflows.

## Tech Stack
- **FastAPI** (Python)
- **LangChain / LLM (Groq)**
- **Google Calendar API**
- **SMTP Email via Outlook**
- **JSON-based in-memory storage**

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/anuhyadasari/ai-scheduling-agent.git
cd ai-scheduling-agent/backend

### 2. Set up the environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

### 3. Create .env file
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=meta-llama/llama-4-scout-17b-16e-instruct

EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USER=your_outlook_email
EMAIL_PASSWORD=your_outlook_password

### 4. Start the server
uvicorn main:app --reload

API Endpoints
POST /ask/ — Chat with the AI assistant
POST /preferences/ — Save scheduling preferences
POST /schedule/ — Trigger meeting invite (Google/Outlook)

Folder Structure
backend/
├── agent.py
├── main.py
├── google_calendar.py
├── outlook_email.py
├── preference_store.py
├── memory_store.py
├── scheduler.py
├── requirements.txt
└── .env

# AI Scheduling Agent – Frontend (React)

This is the React-based frontend for the AI Scheduling Agent. Users can enter preferences, chat with the scheduling agent, and trigger calendar invites.

## Tech Stack
- **React.js**
- **Tailwind CSS**
- **Vite**
- **Axios (API calls)**

## How to Run

### 1. Clone the repo
git clone https://github.com/anuhyadasari/ai-scheduling-agent-frontend.git
cd ai-scheduling-agent-frontend

### 2. Install dependencies
npm install

### 3. Start the app
npm run dev

Backend URL
Update API URLs in ChatInterface.jsx and PreferenceForm.jsx if needed (default: http://localhost:8000).

Folder Structure
src/
├── components/
│   ├── ChatInterface.jsx
│   └── PreferenceForm.jsx
├── App.jsx
├── main.jsx
├── App.css
└── index.css

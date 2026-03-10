# 🏋️ Fitness Coach Agent

An **AI-powered fitness coaching system** that generates workout plans, answers nutrition questions, tracks progress, and remembers user context.

The project is built with a **FastAPI backend**, a **Streamlit frontend**, and an **LLM-powered agent** that can use tools such as workout planning, nutrition guidance, and progress tracking.

The system is designed with a **modular AI agent architecture** similar to production AI systems.

---

# 🚀 Features

### 🤖 AI Fitness Agent

* Conversational AI fitness coach
* Generates personalized workout plans
* Answers fitness and nutrition questions

### 🧠 Memory System

* Stores user conversation context
* Tracks user fitness goals
* Maintains long-term user state

### 🛠 Tool-based Agent

The agent can call specialized tools:

* Workout generation
* Nutrition guidance
* Progress tracking

### 🌐 API Backend

* Built using **FastAPI**
* Clean modular service architecture
* Easy to deploy to cloud environments

### 💬 Telegram Bot

Users can interact with the fitness coach via Telegram.

### 🖥 Web UI

A simple **Streamlit frontend** allows users to interact with the AI coach from a browser.

---

# 🧠 System Architecture

```
User
 │
 ├── Streamlit Web UI
 │
 └── Telegram Bot
       │
       ▼
FastAPI Backend
       │
       ▼
Agent Service
       │
       ▼
Fitness Agent
       │
 ┌─────┴─────┐
 │           │
Tools     Memory
 │           │
Workout   User Context
Nutrition  Progress
Tracking
       │
       ▼
LLM Service
       │
       ▼
OpenRouter API
       │
       ▼
LLM Model (Llama / Gemma)
```

---

# 📂 Project Structure

```
fitness-coach-agent/
│
├── backend/
│
│   ├── main.py                # FastAPI application entrypoint
│   ├── config.py              # Environment configuration
│
│   ├── api/                   # API routes
│   │   └── chat_routes.py
│
│   ├── agent/                 # Core AI agent logic
│   │   ├── fitness_agent.py
│   │   ├── openclaw_agent.py
│   │   └── prompts.py
│
│   ├── services/              # Business logic layer
│   │   ├── agent_service.py
│   │   └── llm_service.py
│
│   ├── memory/                # Memory and persistence
│   │   ├── db.py
│   │   └── user_memory.py
│
│   ├── tools/                 # Agent tools
│   │   ├── workout_tool.py
│   │   ├── nutrition_tool.py
│   │   └── progress_tool.py
│
│   └── bots/
│       └── telegram_bot.py
│
├── frontend/
│   └── streamlit_app.py       # Streamlit user interface
│
├── logs/                      # Application logs
│
├── run.sh                     # Production startup script
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/vboxuser48/fitness-coach-agent.git
cd fitness-coach-agent
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_openrouter_key
TELEGRAM_BOT_TOKEN=your_telegram_token
```

---

# ▶️ Running the Backend

Start the FastAPI server:

```
uvicorn backend.main:app --reload
```

Or run the production script:

```
chmod +x run.sh
./run.sh
```

The API will be available at:

```
http://localhost:8000
```

API docs:

```
http://localhost:8000/docs
```

---

# 🖥 Running the Streamlit Frontend

Start the UI:

```
streamlit run frontend/streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

# 🤖 Running the Telegram Bot

After setting `TELEGRAM_BOT_TOKEN` in `.env`, run:

```
python backend/bots/telegram_bot.py
```

Users can now interact with the fitness coach through Telegram.

---

# 📡 Example API Request

```
POST /chat
```

Example request:

```
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"Create a beginner workout plan"}'
```

Example response:

```
Day 1 – Upper Body Strength
Day 2 – Cardio + Core
Day 3 – Lower Body
Day 4 – Rest
```

---

# 🛠 Tech Stack

* Python
* FastAPI
* Streamlit
* OpenRouter
* LLMs (Llama / Gemma)
* SQLite
* Telegram Bot API

---

# 🌐 Deployment

The backend can be deployed to:

* Railway
* Render
* Fly.io
* Docker

The `run.sh` script starts the production server.

---

# 📌 Future Improvements

* User authentication
* Advanced workout personalization
* Progress analytics dashboard
* Mobile application
* Multi-user training plans

---

# 📄 License

MIT License

from fastapi import FastAPI
from backend.memory.db import init_db
from backend.api.chat_routes import router as chat_router

app = FastAPI(title="Fitness Coach AI Agent")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(chat_router)
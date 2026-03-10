import sqlite3
from backend.config import DATABASE_PATH

def get_connection():
    return sqlite3.connect(DATABASE_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id TEXT PRIMARY KEY,
        goal TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        weight REAL,
        workout_done INTEGER
    )
    """)

    conn.commit()
    conn.close()
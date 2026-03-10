from backend.memory.db import get_connection

def save_weight(user_id, weight):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO progress(user_id, weight, workout_done) VALUES (?, ?, 0)",
        (user_id, weight)
    )

    conn.commit()
    conn.close()


def mark_workout_done(user_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO progress(user_id, weight, workout_done) VALUES (?, NULL, 1)",
        (user_id,)
    )

    conn.commit()
    conn.close()
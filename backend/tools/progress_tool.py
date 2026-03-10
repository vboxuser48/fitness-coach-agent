from backend.memory.user_memory import save_weight, mark_workout_done

def record_weight(user_id, weight):

    save_weight(user_id, weight)

    return f"Weight {weight}kg recorded successfully."


def workout_completed(user_id):

    mark_workout_done(user_id)

    return "Workout recorded. Great consistency!"
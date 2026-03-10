from backend.services.llm_service import chat

def generate_workout(goal):

    system = """
You are a professional fitness trainer.

Create a weekly workout plan.
Include exercises, sets, and reps.
"""

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": goal}
    ]

    return chat(messages)
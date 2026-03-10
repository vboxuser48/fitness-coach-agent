from backend.agent.openclaw_agent import Agent
from backend.agent.prompts import SYSTEM_PROMPT
from backend.services.llm_service import chat

from backend.tools.workout_tool import generate_workout
from backend.tools.nutrition_tool import nutrition_advice
from backend.tools.progress_tool import record_weight, workout_completed


tools = {
    "generate_workout": generate_workout,
    "nutrition_advice": nutrition_advice,
    "record_weight": record_weight,
    "workout_completed": workout_completed
}


def llm(messages):
    return chat(messages)


fitness_agent = Agent(
    name="Fitness Coach",
    instructions=SYSTEM_PROMPT,
    tools=tools,
    llm=llm
)


def run_agent(user_id, message):

    msg = message.lower()

    if "workout" in msg:
        return generate_workout(message)

    if "diet" in msg or "protein" in msg:
        return nutrition_advice(message)

    if "weight" in msg:
        weight = ''.join([c for c in msg if c.isdigit()])
        if weight:
            return record_weight(user_id, float(weight))

    if "done" in msg or "completed" in msg:
        return workout_completed(user_id)

    return fitness_agent.run(message)
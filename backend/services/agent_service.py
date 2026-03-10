from backend.agent.fitness_agent import run_agent

def process_message(user_id, message):

    reply = run_agent(user_id, message)

    return reply
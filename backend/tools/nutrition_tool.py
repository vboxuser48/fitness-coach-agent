from backend.services.llm_service import chat

def nutrition_advice(question):

    system = """
You are a nutrition expert.

Answer clearly and concisely.
Focus on fitness and diet.
"""

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": question}
    ]

    return chat(messages)
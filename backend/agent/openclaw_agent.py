class Agent:

    def __init__(self, name, instructions, tools, llm):
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.llm = llm

    def run(self, input, context=None):

        messages = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": input},
        ]

        response = self.llm(messages)

        return response
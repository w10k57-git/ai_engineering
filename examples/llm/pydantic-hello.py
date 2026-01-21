from dotenv import load_dotenv
from pydantic_ai import Agent, ModelSettings

load_dotenv()

agent = Agent(
    "groq:llama-3.3-70b-versatile",
    instructions="""
    Your task is to evaluate, whether the statement provided
    by the user is True or False. YOU MUST ANSWER WITH EITHER
    "True" or "False" and nothing else.
    """,
    model_settings=ModelSettings(max_tokens=1, temperature=0.2),
)

question = "Earth is a geoid"

result = agent.run_sync(question)
print(result.output)

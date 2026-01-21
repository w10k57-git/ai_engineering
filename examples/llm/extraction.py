from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent

load_dotenv()


class ExtractionOutput(BaseModel):
    names: list[str] = Field(..., description="A list of names mentioned in the text.")
    locations: list[str] = Field(
        ..., description="A list of locations mentioned in the text."
    )


agent = Agent(
    "ollama:qwen3:4b",
    instructions="""
    Your task is to extract all the names and locations 
    from the text the user inputs.
    """,
    output_type=ExtractionOutput,
)

question = "Barack Obama was born in Hawaii and lived in Chicago."

result = agent.run_sync(question)
entities = result.output
print("Names:", entities.names)
print("Locations:", entities.locations)

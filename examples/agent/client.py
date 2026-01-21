import asyncio

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

load_dotenv()


async def main():
    print("Starting Engineering Calculator MCP Client...")
    print("-" * 60)

    # Create MCP server connection using stdio transport
    # The server is run as a subprocess
    server = MCPServerStdio("python", args=["examples/agent/server.py"], timeout=10)

    agent = Agent("ollama:qwen3:4b", toolsets=[server])

    # Use context manager to handle server connection lifecycle
    async with agent:
        print("\n1. Calculating stress for a structural beam:")
        print("   Force: 50,000 N, Area: 0.002 m²")
        result1 = await agent.run(
            "Calculate the stress when a force of 50000 Newtons is applied "
            "over an area of 0.002 square meters"
        )
        print(f"   Result: {result1.output}\n")

        print("2. Calculating RPM for a rotating shaft:")
        print("   Angular velocity: 157.08 rad/s")
        result2 = await agent.run("What is the RPM when the angular velocity is 157.08 rad/s?")
        print(f"   Result: {result2.output}\n")

        print("3. Combined engineering problem:")
        result3 = await agent.run(
            "A motor shaft rotates at 31.416 rad/s. What is its RPM? "
            "Also, if this shaft transmits a force of 10000 N through a "
            "cross-section of 0.001 m², what is the stress?"
        )
        print(f"   Result: {result3.output}\n")

    print("-" * 60)
    print("Client demonstration completed successfully!")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())

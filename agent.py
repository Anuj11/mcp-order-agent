import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()
SERVER_PATH = Path(__file__).with_name("server.py")


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "orders": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(SERVER_PATH)],
            }
        }
    )

    tools = await client.get_tools()
    print("Available tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

    model_name = os.getenv("MODEL_NAME", "openai:gpt-4.1-mini")
    agent = create_agent(
        model=model_name,
        tools=tools,
        system_prompt=(
            "You are a helpful order-support assistant. "
            "Use the order tool to answer order questions. "
            "Never invent order details. If an order is not found, "
            "clearly say that it could not be found."
        ),
    )

    order_id = os.getenv("DEMO_ORDER_ID", "1024")
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"Where is my order number {order_id}?",
                }
            ]
        }
    )

    print("\nAssistant:")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())

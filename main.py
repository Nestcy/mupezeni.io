import asyncio

from app.mcp.transport import discover_tools
from app.runtime.agent import build_agent, run_agent


async def main():
    print("Connecting to commerce MCP server...", flush=True)

    # Keep the client alive while the agent uses its tools.
    mcp_client, tools = await discover_tools()

    print(
        f"Approved tools: {[tool.name for tool in tools]}",
        flush=True,
    )

    agent = build_agent(tools=tools)

    print("\nMupezeni is ready.", flush=True)

    response = await run_agent(
        agent,
        "Search the product catalog for black sneakers. "
        "Use the search_products tool to find matching products. "
        "Report the product names, prices, and currency based only "
        "on the tool results.",
    )

    print("\nAgent response:", flush=True)
    print(response, flush=True)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from app.mcp.transport import discover_tools


async def main():
    # Approve only the read-only demo search tool.
    client, tools = await discover_tools(
        allowed_tool_names={"search_products"}
    )

    print(f"\nApproved tools: {[tool.name for tool in tools]}")

    if not tools:
        raise RuntimeError(
            "No approved tools found. Check the discovered names."
        )

    result = await tools[0].ainvoke(
        {"query": "sneakers", "limit": 5}
    )

    print("\nTool result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

from langchain_mcp_adapters.client import MultiServerMCPClient


COMMERCE_SERVER_URL = "http://127.0.0.1:8001/mcp"

ALLOWED_TOOL_NAMES = {
    "search_products",
}


async def discover_tools():
    client = MultiServerMCPClient(
        {
            "commerce": {
                "transport": "streamable_http",
                "url": COMMERCE_SERVER_URL,
            }
        }
    )

    discovered_tools = await client.get_tools()

    print("Discovered MCP tools:", flush=True)
    for tool in discovered_tools:
        print(f"- {tool.name}", flush=True)

    approved_tools = [
        tool
        for tool in discovered_tools
        if tool.name in ALLOWED_TOOL_NAMES
    ]

    if not approved_tools:
        raise RuntimeError(
            "No approved commerce tools found. "
            "Check the MCP server and discovered tool names."
        )

    return client, approved_tools

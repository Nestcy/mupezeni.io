from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mupezeni Commerce")

# Demo data only. Replace this with your real store adapter later.
DEMO_PRODUCTS = [
    {
        "id": "demo-001",
        "name": "Classic Black Sneakers",
        "category": "Footwear",
        "price": 450,
        "currency": "ZMW",
    },
    {
        "id": "demo-002",
        "name": "Brown Leather Handbag",
        "category": "Accessories",
        "price": 650,
        "currency": "ZMW",
    },
    {
        "id": "demo-003",
        "name": "White Cotton T-Shirt",
        "category": "Clothing",
        "price": 180,
        "currency": "ZMW",
    },
]


@mcp.tool()
def search_products(query: str, limit: int = 5) -> dict:
    """Search the demo product catalog by product name or category."""

    if not 1 <= limit <= 10:
        return {"error": "Limit must be between 1 and 10."}

    query = query.strip().lower()

    if not query:
        return {"products": []}

    matches = [
        product
        for product in DEMO_PRODUCTS
        if query in product["name"].lower()
        or query in product["category"].lower()
    ]

    return {
        "source": "demo_catalog",
        "products": matches[:limit],
        "count": min(len(matches), limit),
    }


if __name__ == "__main__":
    mcp.settings.host = "127.0.0.1"
    mcp.settings.port = 8001
    mcp.run(transport="streamable-http")

# pyrefly: ignore[missing-import]
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Order Support")

# Demo-only data. Replace this with an authenticated business service in production.
ORDERS = {
    "1024": {
        "product": "Wireless headphones",
        "status": "shipped",
        "estimated_delivery": "Friday",
    },
    "1025": {
        "product": "Mechanical keyboard",
        "status": "processing",
        "estimated_delivery": "Next Tuesday",
    },
}


@mcp.tool()
def get_order_status(order_id: str) -> dict:
    """Get the status and delivery estimate for an order."""

    order = ORDERS.get(order_id)
    if order is None:
        return {
            "found": False,
            "order_id": order_id,
            "message": "Order not found",
        }

    return {
        "found": True,
        "order_id": order_id,
        **order,
    }


if __name__ == "__main__":
    # stdio is suitable for this local client-launched demo.
    mcp.run(transport="stdio")

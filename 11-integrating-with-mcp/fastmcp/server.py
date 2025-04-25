# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀",host="10.239.1.236",port=9003)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def get_current_time(timezone: str) -> dict:
    """Get current time in a specific timezone."""
    from datetime import datetime
    import pytz

    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    return {
        "timezone": timezone,
        "datetime": now.isoformat(timespec="seconds"),
        "is_dst": bool(now.dst()),
    }

@mcp.tool()
def get_data_from_api(api_url: str) -> str:
    """Fetch data from a given API URL."""
    import requests

    response = requests.get(api_url)
    if response.status_code == 200:
        return "ok"
    else:
        return "error"

if __name__ == "__main__":
    mcp.run(transport="sse")
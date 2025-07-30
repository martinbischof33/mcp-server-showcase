# MCP library
from mcp.server.fastmcp import FastMCP
from models.models import AddResponse

API_BASE_URL = "http://192.168.1.76:8888"

# API endpoint for diverse requests
DIVERSE_REQUEST_ENDPOINT = API_BASE_URL + "/api/v1/prc/diverse-requests/"

# MCP server instance
mcp = FastMCP(
    name="Sandrock und Partner Terminangelegenheiten und Empfang",

    instructions="""Description""",

    host="0.0.0.0",
    port=9000,
    transport="streamable-http"
)


@mcp.tool(name="add")
def add(a: int, b: int) -> AddResponse: 
    """
    add two numbers
    """
    
    return AddResponse(result=a + b)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
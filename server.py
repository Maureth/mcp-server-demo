# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b

### Resources ###
@mcp.resource("resource://some_static_resource")
def get_static_resource() -> str:
    """Static resource data"""
    return "Any static data can be returned"

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

### Prompts ###
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    return[
        ("user", "I'm seeing this error:"),
        ("user", error),
        ("assistant", "I'll help you debug that. Wht hace youy tried so far?"),
    ]

if __name__ == "__main__":
    #inicialize and run the server
    mcp.run(transport="sse")


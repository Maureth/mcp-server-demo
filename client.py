from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            # #list available tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            #call a tool
            result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print("Result:", result.content[0].text)
            resources = await session.list_resources()
            print("Available resources:", resources)

            # Read a resource
            content = await session.read_resource("resource://some_static_resource")
            print("content", content.contents[0].text)

            # Read a resource
            content = await session.read_resource("greeting://mau")
            print("content", content.contents[0].text)

            # List available prompts
            prompts = await session.list_prompts()
            print("Available prompts:", prompts)

            # Get a prompt
            prompt = await session.get_prompt(
                "review_code", arguments={"code": "print('Hello, world!')"},
            )
            print("Prompt:", prompt)

            prompt = await session.get_prompt(
                "debug_error", arguments={"error": "SyntaxError: invalid syntax"},
            )
            print("Prompt:", prompt)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())


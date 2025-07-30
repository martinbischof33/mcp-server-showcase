#!/usr/bin/env python3
"""
mcp_test_client.py

A full example MCP client that:
1. Connects via Streamable HTTP
2. Initializes the MCP session
3. Lists available prompts, resources, and tools
"""

import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp.client.session import ClientSession

# Replace with your MCP server endpoint
SERVER_URL = "http://185.55.243.159:9000/mcp/"

async def main():
    # Establish Streamable HTTP client streams
    async with streamablehttp_client(SERVER_URL) as (read_stream, write_stream, _):
        # Create and initialize the MCP session
        async with ClientSession(read_stream, write_stream) as session:
            init_resp = await session.initialize()
            print("Session initialized:", init_resp)  # includes server name and version

            # List prompts
            prompts = await session.list_prompts()
            print("\nAvailable Prompts:")
            for p in prompts:
                if hasattr(p, 'name'):
                    print(f"  • {p.name}: {getattr(p, 'description', 'No description')}")
                else:
                    print(f"  • {p}")

            # List resources
            resources = await session.list_resources()
            print("\nAvailable Resources:")
            for r in resources:
                if hasattr(r, 'name'):
                    print(f"  • {r.name}")
                else:
                    print(f"  • {r}")

            # List tools
            tools = await session.list_tools()
            print("\nAvailable Tools:")
            for t in tools:
                if hasattr(t, 'name'):
                    print(f"  • {t.name}: {getattr(t, 'description', 'No description')}")
                else:
                    print(f"  • {t}")

if __name__ == "__main__":
    asyncio.run(main())

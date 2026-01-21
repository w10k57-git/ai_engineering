# AI Agent with MCP shared tools

To expose tools listed in `tools.py`, you have to add the MCP server to the `mcp.json` file in the client application. The content to add is:

```json
{
  "mcpServers": {
    "eng_tools": {
      "url": "http://127.0.0.1:8021/mcp"
    }
  }
}
```

Before you use the server, you need to run it by using (from the repo root): `uv run python examples/agent/tools.py`.

from mcp_organizze.server import mcp
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="MCP Organizze Server")
    parser.add_argument("--transport", choices=["stdio", "streamable-http"], default="stdio", help="Transport mode")
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP server")
    parser.add_argument("--port", type=int, default=8000, help="Port for HTTP server")

    args = parser.parse_args()

    print(f"Iniciando MCP Organizze em modo '{args.transport}'...", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)

if __name__ == "__main__":
    main()

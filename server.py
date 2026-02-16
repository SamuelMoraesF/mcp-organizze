
from fastmcp import FastMCP
import yaml
import httpx
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Carregar especificação OpenAPI
try:
    with open("openapi.yaml", "r") as f:
        openapi_spec = yaml.safe_load(f)
except FileNotFoundError:
    print("Erro: openapi.yaml não encontrado.")
    exit(1)

# Configurar credenciais
email = os.environ.get("ORGANIZZE_EMAIL")
api_key = os.environ.get("ORGANIZZE_API_KEY")
user_agent_custom = os.environ.get("USER_AGENT", f"MCP-Organizze (samuel@samuelmoraes.com)")

if not email or not api_key:
    print("AVISO: Variáveis de ambiente ORGANIZZE_EMAIL e ORGANIZZE_API_KEY não encontradas.")

# Cliente HTTP Assíncrono com Autenticação Básica (apenas se credenciais existirem)
client = httpx.AsyncClient(
    base_url="https://api.organizze.com.br/rest/v2",
    auth=(email, api_key) if email and api_key else None,
    headers={
        "User-Agent": user_agent_custom,
        "Content-Type": "application/json"
    },
    timeout=30.0
)

# Criar Servidor MCP dinâmico
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Organizze API"
)

if __name__ == "__main__":
    mcp.run()

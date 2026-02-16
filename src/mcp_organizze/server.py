import yaml
import httpx
import os
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# Carregar especificação OpenAPI usando caminho relativo
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    openapi_path = os.path.join(current_dir, "openapi.yaml")
    with open(openapi_path, "r") as f:
        openapi_spec = yaml.safe_load(f)
except FileNotFoundError:
    # Fallback para execução local de teste onde openapi.yaml pode estar no CWD
    try:
        with open("openapi.yaml", "r") as f:
            openapi_spec = yaml.safe_load(f)
    except FileNotFoundError:
        import sys
        print(f"Erro: openapi.yaml não encontrado em {openapi_path} ou no diretório atual.", file=sys.stderr)
        sys.exit(1)

# Configurar credenciais
email = os.environ.get("ORGANIZZE_EMAIL")
api_key = os.environ.get("ORGANIZZE_API_KEY")
user_agent_custom = os.environ.get("USER_AGENT", f"MCP-Organizze ({email or 'unknown'})")

if not email or not api_key:
    import sys
    print("AVISO: Variáveis de ambiente ORGANIZZE_EMAIL e ORGANIZZE_API_KEY não encontradas.", file=sys.stderr)

client = httpx.AsyncClient(
    base_url="https://api.organizze.com.br/rest/v2",
    auth=(email, api_key) if email and api_key else None,
    headers={
        "User-Agent": user_agent_custom,
        "Content-Type": "application/json"
    },
    timeout=30.0
)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Organizze API"
)

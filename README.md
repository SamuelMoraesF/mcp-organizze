[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/samuelmoraesf-mcp-organizze-badge.png)](https://mseep.ai/app/samuelmoraesf-mcp-organizze)

# MCP Organizze

Servidor MCP para integração com o gestor financeiro Organizze, compatível com qualquer cliente MCP (Claude Desktop, etc).

Este projeto expõe a API v2 do Organizze como ferramentas de IA, permitindo criar transações, consultar saldos, metas e muito mais.

## ✨ Funcionalidades

- **Contas**: Listar, criar e detalhar contas bancárias.
- **Transações**: Criar (despesas/receitas) e listar movimentações.
- **Cartões de Crédito**: Listar e detalhar faturas.
- **Categorias e Metas**: Gerenciamento completo.

## 🚀 Como Usar

### Pré-requisitos

Você precisará das suas credenciais do Organizze:
- `ORGANIZZE_EMAIL`: Seu email de login.
- `ORGANIZZE_API_KEY`: Sua chave de API.

### Opção 1: Via UVX (Recomendado)

Se você tem o `uv` instalado, pode rodar diretamente sem instalar nada:

```bash
# Executa em modo STDIO (padrão para Claude Desktop)
ORGANIZZE_EMAIL=seu@email.com ORGANIZZE_API_KEY=sua_chave uvx mcp-organizze
```

Para integrar ao **Claude Desktop**, adicione ao seu arquivo de configuração:

```json
{
  "mcpServers": {
    "organizze": {
      "command": "uvx",
      "args": ["mcp-organizze"],
      "env": {
        "ORGANIZZE_EMAIL": "seu_email",
        "ORGANIZZE_API_KEY": "sua_chave_api"
      }
    }
  }
}
```

### Opção 2: Via Docker

A imagem Docker roda por padrão em modo **Streamable HTTP (SSE)** na porta 8000, ideal para uso remoto ou em servidores.

**Executar com SSE (Porta 8000):**

```bash
docker run -p 8000:8000 \
  -e ORGANIZZE_EMAIL=seu_email \
  -e ORGANIZZE_API_KEY=sua_chave \
  mcp-organizze
```

**Executar com STDIO (Interativo):**

```bash
docker run -i \
  -e ORGANIZZE_EMAIL=seu_email \
  -e ORGANIZZE_API_KEY=sua_chave \
  mcp-organizze --transport stdio
```

### Opção 3: Instalação Local (Pip/UV)

Clone o repositório e instale:

```bash
uv pip install .
# ou
pip install .
```

Rode o servidor:
```bash
python -m mcp_organizze
```

## 🛠 Desenvolvimento e Publicação

### Estrutura do Projeto

- `src/mcp_organizze`: Código fonte do pacote.
- `pyproject.toml`: Configuração de build e dependências.
- `Dockerfile`: Configuração para containerização.
- `.github/workflows`: Actions para CI/CD.

<!-- mcp-name: io.github.SamuelMoraesF/mcp-organizze -->
FROM python:3.11-slim-bookworm
LABEL io.modelcontextprotocol.server.name="io.github.SamuelMoraesF/mcp-organizze"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

RUN useradd -m organizze
USER organizze

EXPOSE 8000

ENTRYPOINT ["python3", "-m", "mcp_organizze"]
CMD ["--transport", "streamable-http", "--host", "0.0.0.0", "--port", "8000"]

# Dockerfile para o Busca-PC com Python e UV
FROM python:3.13-slim

WORKDIR /app

# Instalar dependências de sistema mínimas para compilação e rede
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar o uv (gerenciador ultrarrápido de pacotes Python)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copiar arquivos de dependências
COPY pyproject.toml uv.lock ./

# Instalar dependências sem instalar o projeto raiz ainda
RUN uv sync --frozen --no-install-project

# Copiar o código fonte e assets
COPY src/ ./src/
COPY knowledge_base/ ./knowledge_base/
COPY main.py README.md ./

# Instalar o próprio pacote busca-pc no ambiente
RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src:$PYTHONPATH"
ENV RUNNING_IN_DOCKER="true"
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Inicializa o servidor web ASGI
CMD ["uvicorn", "busca_pc.web.app:app", "--host", "0.0.0.0", "--port", "8000"]

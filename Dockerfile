# ── Imagem base ──────────────────────────────────────────────
FROM python:3.12-slim

# Evita prompts interativos e garante saída imediata no log
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ── Diretório de trabalho ────────────────────────────────────
WORKDIR /app

# ── Dependências Python ──────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Código-fonte ─────────────────────────────────────────────
COPY . .

# ── Porta exposta ────────────────────────────────────────────
EXPOSE 5000

# ── Inicialização ────────────────────────────────────────────
CMD ["python", "main.py"]

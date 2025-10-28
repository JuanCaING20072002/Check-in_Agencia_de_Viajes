# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dependencias del sistema para compilar paquetes (psycopg2) y libpq
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install -r requirements.txt

# Crea usuario no-root
RUN useradd -m -u 10001 appuser

# Copia el código y el entrypoint
COPY . /app
RUN chmod +x /app/entrypoint.sh \
 && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000
ENV PORT=5000

ENTRYPOINT ["/app/entrypoint.sh"]

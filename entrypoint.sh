#!/usr/bin/env sh
set -e

# Variables por defecto
export FLASK_APP="${FLASK_APP:-app.py}"
export FLASK_ENV="${FLASK_ENV:-production}"

# Espera opcional a la base de datos si DATABASE_URL está definido
python - <<'PY'
import os, sys, time, socket, urllib.parse
url = os.environ.get('DATABASE_URL')
if not url:
    sys.exit(0)
p = urllib.parse.urlparse(url)
host = p.hostname or 'localhost'
port = p.port or 5432
for i in range(60):
    try:
        with socket.create_connection((host, port), 2):
            sys.exit(0)
    except OSError:
        time.sleep(1)
print("La base de datos no respondió a tiempo", file=sys.stderr)
sys.exit(1)
PY

# Aplica migraciones si está Flask CLI
if command -v flask >/dev/null 2>&1; then
  flask db upgrade || true
fi

# Arranca Gunicorn
exec gunicorn -w ${GUNICORN_WORKERS:-3} -b 0.0.0.0:${PORT:-5000} app:app

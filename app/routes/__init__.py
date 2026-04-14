"""Routes/Blueprints module."""
from flask import Blueprint

# Initialize blueprints
main_bp = Blueprint("main", __name__)
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
viajes_bp = Blueprint("viajes", __name__, url_prefix="/viajes")
reservas_bp = Blueprint("reservas", __name__, url_prefix="/reservas")
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Import route handlers to register them
from app.routes import admin, auth, main, reservas, viajes

__all__ = ["main_bp", "auth_bp", "viajes_bp", "reservas_bp", "admin_bp"]

"""Admin routes - requires admin role."""
from functools import wraps

from flask import abort, render_template
from flask_login import current_user

from app.routes import admin_bp
from app.services import viaje_service, auth_service, reserva_service


def admin_required(f):
    """Decorator to require admin role."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            abort(403)
        return f(*args, **kwargs)

    return decorated_function


@admin_bp.route("/dashboard", methods=["GET"])
@admin_required
def dashboard():
    """Admin dashboard."""
    viajes_count = len(viaje_service.get_all())
    usuarios_count = len(auth_service.get_all())
    reservas_count = len(reserva_service.get_all())

    return render_template(
        "admin/dashboard.html",
        viajes_count=viajes_count,
        usuarios_count=usuarios_count,
        reservas_count=reservas_count,
    )

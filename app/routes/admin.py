"""Admin routes - requires admin role."""
from functools import wraps

from flask import abort, render_template

from app.routes import admin_bp


def admin_required(f):
    """Decorator to require admin role."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from flask_login import current_user

        if not current_user.is_authenticated or not current_user.is_admin():
            abort(403)
        return f(*args, **kwargs)

    return decorated_function


@admin_bp.route("/dashboard", methods=["GET"])
@admin_required
def dashboard():
    """Admin dashboard."""
    from app.models import Reserva, Usuario, Viaje

    viajes_count = Viaje.query.count()
    usuarios_count = Usuario.query.count()
    reservas_count = Reserva.query.count()

    return render_template(
        "admin/dashboard.html",
        viajes_count=viajes_count,
        usuarios_count=usuarios_count,
        reservas_count=reservas_count,
    )

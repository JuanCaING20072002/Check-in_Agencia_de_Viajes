"""Viajes routes."""
from flask import render_template
from flask_login import login_required

from app.routes import viajes_bp
from app.services import viaje_service


@viajes_bp.route("/", methods=["GET"])
def listar():
    """List all trips."""
    viajes = viaje_service.get_all()
    return render_template("viajes/listar.html", viajes=viajes)


@viajes_bp.route("/<int:viaje_id>", methods=["GET"])
@login_required
def detalle(viaje_id: int):
    """Trip detail page."""
    viaje = viaje_service.get_by_id(viaje_id)

    if not viaje:
        return "Viaje no encontrado", 404

    return render_template("viajes/detalle.html", viaje=viaje)

"""Viajes routes."""
from app.routes import viajes_bp


@viajes_bp.route("/", methods=["GET"])
def listar():
    """List all trips."""
    from flask import render_template

    from app.models import Viaje

    viajes = Viaje.query.all()
    return render_template("viajes/listar.html", viajes=viajes)


@viajes_bp.route("/<int:viaje_id>", methods=["GET"])
def detalle(viaje_id: int):
    """Trip detail page."""
    from flask import render_template

    from app.models import Viaje

    viaje = Viaje.query.get_or_404(viaje_id)
    return render_template("viajes/detalle.html", viaje=viaje)

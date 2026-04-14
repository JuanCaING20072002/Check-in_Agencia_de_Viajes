"""Reservas routes."""
from app.routes import reservas_bp


@reservas_bp.route("/", methods=["GET"])
def listar():
    """List reservations."""
    from flask import render_template
    from flask_login import login_required

    from app.models import Reserva

    reservas = Reserva.query.all()
    return render_template("reservas/listar.html", reservas=reservas)


@reservas_bp.route("/nueva/<int:viaje_id>", methods=["GET", "POST"])
def nueva(viaje_id: int):
    """Create new reservation."""
    from flask import redirect, render_template, request, url_for, flash

    from app.extensions import db
    from app.models import Reserva, Viaje

    viaje = Viaje.query.get_or_404(viaje_id)

    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        fecha = request.form.get("fecha")
        mensaje = request.form.get("mensaje")

        if not nombre or not email:
            flash("Por favor completa nombre y correo.")
            return redirect(url_for("reservas.nueva", viaje_id=viaje_id))

        reserva = Reserva(
            nombre=nombre,
            email=email,
            fecha=fecha or "",
            mensaje=mensaje or "",
            viaje_id=viaje_id,
        )
        db.session.add(reserva)
        db.session.commit()

        flash("¡Reserva creada exitosamente!")
        return redirect(url_for("viajes.listar"))

    return render_template("reservas/nueva.html", viaje=viaje)

"""Reservas routes."""

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.routes import reservas_bp
from app.services import email_service, reserva_service, viaje_service


@reservas_bp.route("/", methods=["GET"])
@login_required
def listar():
    """List reservations."""
    reservas = reserva_service.get_all()
    return render_template("reservas/listar.html", reservas=reservas)


@reservas_bp.route("/nueva/<int:viaje_id>", methods=["GET", "POST"])
@login_required
def nueva(viaje_id: int):
    """Create new reservation."""
    viaje = viaje_service.get_by_id(viaje_id)

    if not viaje:
        flash("Viaje no encontrado.")
        return redirect(url_for("viajes.listar"))

    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        fecha = request.form.get("fecha", "")
        mensaje = request.form.get("mensaje", "")

        try:
            if not nombre or not email:
                flash("Por favor completa nombre y correo.")
                return redirect(url_for("reservas.nueva", viaje_id=viaje_id))

            # Create reservation using service
            reserva = reserva_service.create(
                nombre=nombre,
                email=email,
                fecha=fecha,
                mensaje=mensaje,
                viaje_id=viaje_id,
            )

            # Send confirmation email
            email_service.send_reservation_confirmation(email, nombre, viaje.nombre)

            flash("¡Reserva creada exitosamente!")
            return redirect(url_for("viajes.listar"))

        except ValueError as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for("reservas.nueva", viaje_id=viaje_id))

    return render_template("reservas/nueva.html", viaje=viaje)

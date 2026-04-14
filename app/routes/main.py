"""Main routes."""

from flask import render_template

from app.routes import main_bp


@main_bp.route("/")
def index():
    """Home page."""
    return render_template("index.html")


@main_bp.route("/nosotros")
def nosotros():
    """About page."""
    return render_template("nosotros.html")


@main_bp.route("/enviar-respuesta", methods=["POST"])
def enviar_respuesta():
    """Handle form submission."""
    from flask import flash, redirect, request, url_for

    nombre = request.form.get("nombre")
    email = request.form.get("email")
    experiencias = request.form.getlist("experiencia")

    if not nombre or not email:
        flash("Por favor completa nombre y correo.")
        return redirect(url_for("main.index"))

    return render_template("gracias.html", nombre=nombre, email=email, experiencias=experiencias)

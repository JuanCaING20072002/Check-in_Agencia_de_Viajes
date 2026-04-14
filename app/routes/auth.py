"""Authentication routes."""
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from app.routes import auth_bp
from app.services import auth_service, email_service


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login route."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            usuario = auth_service.login(username, password)

            if usuario:
                login_user(usuario)
                flash(f"¡Bienvenido, {usuario.username}!")
                return redirect(url_for("main.index"))
            else:
                flash("Usuario o contraseña inválidos.")
        except ValueError as e:
            flash(f"Error: {str(e)}")

    return render_template("login.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """Logout route."""
    logout_user()
    return redirect(url_for("main.index"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registration route."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        try:
            if not username or not password:
                flash("Por favor completa todos los campos.")
                return redirect(url_for("auth.register"))

            if password != password_confirm:
                flash("Las contraseñas no coinciden.")
                return redirect(url_for("auth.register"))

            # Use service to register
            usuario = auth_service.create(username, password)

            # Send welcome email
            email_service.send_welcome_email(username, username)

            login_user(usuario)
            flash("¡Registro exitoso!")
            return redirect(url_for("main.index"))

        except ValueError as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for("auth.register"))

    return render_template("register.html")

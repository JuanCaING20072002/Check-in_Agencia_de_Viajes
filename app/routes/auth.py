"""Authentication routes."""
from app.routes import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login route."""
    from flask import flash, redirect, render_template, request, url_for
    from flask_login import login_user

    from app.models import Usuario

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Por favor proporciona usuario y contraseña.")
            return redirect(url_for("auth.login"))

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password):
            login_user(usuario)
            flash(f"¡Bienvenido, {usuario.username}!")
            return redirect(url_for("main.index"))
        else:
            flash("Usuario o contraseña inválidos.")

    return render_template("login.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """Logout route."""
    from flask import redirect, url_for
    from flask_login import logout_user

    logout_user()
    return redirect(url_for("main.index"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registration route."""
    from flask import flash, redirect, render_template, request, url_for
    from flask_login import login_user

    from app.extensions import db
    from app.models import Usuario

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        if not username or not password:
            flash("Por favor completa todos los campos.")
            return redirect(url_for("auth.register"))

        if password != password_confirm:
            flash("Las contraseñas no coinciden.")
            return redirect(url_for("auth.register"))

        if Usuario.query.filter_by(username=username).first():
            flash("El usuario ya existe.")
            return redirect(url_for("auth.register"))

        usuario = Usuario(username=username)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()

        login_user(usuario)
        flash("¡Registro exitoso!")
        return redirect(url_for("main.index"))

    return render_template("register.html")

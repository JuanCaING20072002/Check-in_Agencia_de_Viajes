"""Flask application factory."""
import os

from flask import Flask
from flask_migrate import Migrate

from app.config import get_config
from app.extensions import db, login_manager, migrate
from app.models import Reserva, Usuario, Viaje


def create_app(config_name: str = None) -> Flask:
    """
    Create and configure the Flask application.
    
    Args:
        config_name: Configuration class name ('development', 'testing', 'production')
        
    Returns:
        Configured Flask app instance
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    config = get_config()
    app.config.from_object(config)

    # Set database URI
    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        app.config["SQLALCHEMY_DATABASE_URI"] = config.get_database_url()

    # Add PostgreSQL-specific engine options (not for SQLite)
    db_url = app.config.get("SQLALCHEMY_DATABASE_URI", "")
    if not db_url.startswith("sqlite"):
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "pool_pre_ping": True,
            "pool_size": int(os.environ.get("SQLALCHEMY_POOL_SIZE", 5)),
            "max_overflow": int(os.environ.get("SQLALCHEMY_MAX_OVERFLOW", 10)),
            "pool_recycle": int(os.environ.get("SQLALCHEMY_POOL_RECYCLE", 1800)),
        }

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register user loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id: str) -> Usuario | None:
        try:
            return Usuario.query.get(int(user_id))
        except Exception:
            return None

    # Register error handlers
    register_error_handlers(app)

    # Create tables and register blueprints within context
    with app.app_context():
        # Create all database tables
        db.create_all()

        # Health check endpoint
        @app.route("/health")
        def health():
            return {"status": "ok"}, 200

        # Register blueprints
        from app.routes import admin_bp, auth_bp, main_bp, reservas_bp, viajes_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(viajes_bp)
        app.register_blueprint(reservas_bp)
        app.register_blueprint(admin_bp)

    return app


def register_error_handlers(app: Flask) -> None:
    """Register error handlers."""
    from sqlalchemy.exc import OperationalError

    @app.errorhandler(OperationalError)
    def handle_db_operational_error(error):
        """Handle database operational errors."""
        app.logger.exception(f"Database error: {error}")
        return (
            {
                "error": "Servicio temporalmente no disponible",
                "detail": "Por favor intenta más tarde.",
            },
            503,
        )

    @app.errorhandler(403)
    def forbidden(error):
        """Handle 403 Forbidden."""
        return {"error": "Acceso denegado"}, 403

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 Not Found."""
        return {"error": "Página no encontrada"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 Internal Server Error."""
        app.logger.exception(f"Internal error: {error}")
        return {"error": "Error interno del servidor"}, 500

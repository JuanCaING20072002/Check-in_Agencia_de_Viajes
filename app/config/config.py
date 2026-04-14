"""
Application configuration module.
Handles different environments: development, testing, production.
"""
import os
from datetime import timedelta
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


class Config:
    """Base configuration class."""

    # Flask
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {}

    # Session
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True

    # Upload
    UPLOAD_FOLDER = os.path.join("static", "img")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

    # SMTP Email
    SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("SMTP_USER", "")
    SMTP_PASS = os.environ.get("SMTP_PASS", "")

    # Reset Token
    RESET_TOKEN_SALT = os.environ.get("RESET_TOKEN_SALT", "reset-password-salt")

    @staticmethod
    def get_database_url() -> str:
        """
        Resolve database URI from environment variables.
        Tries multiple common variable names and normalizes the URL.
        """
        keys = ["DATABASE_URL", "DATABASE_URI", "POSTGRES_URL", "POSTGRES_URI"]

        for key in keys:
            db_url = os.environ.get(key)
            if db_url:
                # Normalize postgres:// to postgresql://
                if db_url.startswith("postgres://"):
                    db_url = "postgresql://" + db_url[len("postgres://"):]

                # Parse and rebuild URL safely
                try:
                    parsed = urlparse(db_url)
                    scheme = parsed.scheme
                    netloc = parsed.netloc
                    path = parsed.path
                    params = parsed.params
                    query_items = dict(
                        parse_qsl(parsed.query, keep_blank_values=True)
                    )

                    # Add sslmode for cloud providers (e.g., Neon)
                    hostname = parsed.hostname or ""
                    if (
                        hostname.endswith(".neon.tech")
                        and "sslmode" not in query_items
                    ):
                        query_items["sslmode"] = "require"

                    new_query = urlencode(query_items, doseq=True)
                    rebuilt = urlunparse(
                        (scheme, netloc, path, params, new_query, parsed.fragment)
                    )
                    return rebuilt
                except Exception:
                    return db_url

        # Fallback to traditional PostgreSQL environment variables
        db_user = os.environ.get("POSTGRES_USER", "postgres")
        db_pass = os.environ.get("POSTGRES_PW", "12345")
        db_host = os.environ.get("POSTGRES_HOST", "localhost")
        db_port = os.environ.get("POSTGRES_PORT", "5432")
        db_name = os.environ.get("POSTGRES_DB", "reservasdb")

        return (
            f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        )


class DevelopmentConfig(Config):
    """Development environment configuration."""

    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False


class TestingConfig(Config):
    """Testing environment configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production environment configuration."""

    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


def get_config():
    """Get configuration object based on FLASK_ENV."""
    env = os.environ.get("FLASK_ENV", "development").lower()
    
    config_map = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    
    return config_map.get(env, DevelopmentConfig)

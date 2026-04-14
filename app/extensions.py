"""Flask extensions initialization."""

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Configure login manager
login_manager.login_view = "auth.login"
login_manager.login_message = "Por favor inicia sesión para continuar."
login_manager.login_message_category = "info"

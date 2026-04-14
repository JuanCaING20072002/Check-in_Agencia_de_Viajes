"""Authentication service."""

from typing import Optional, Tuple

from app.extensions import db
from app.models import Usuario
from app.services.base_service import BaseService


class AuthService(BaseService):
    """Service for authentication operations."""

    def create(self, username: str, password: str, rol: str = "usuario") -> Usuario:
        """Register a new user."""
        self._validate_required_fields(
            {"username": username, "password": password},
            ["username", "password"],
        )

        # Check if user already exists
        if Usuario.query.filter_by(username=username).first():
            raise ValueError(f"Usuario '{username}' ya existe")

        # Create new user
        usuario = Usuario(username=username, rol=rol)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()

        return usuario

    def login(self, username: str, password: str) -> Optional[Usuario]:
        """Authenticate user by username and password."""
        self._validate_required_fields(
            {"username": username, "password": password},
            ["username", "password"],
        )

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password):
            return usuario

        return None

    def get_by_id(self, user_id: int) -> Optional[Usuario]:
        """Get user by ID."""
        return Usuario.query.get(user_id)

    def get_by_username(self, username: str) -> Optional[Usuario]:
        """Get user by username."""
        return Usuario.query.filter_by(username=username).first()

    def get_all(self) -> list:
        """Get all users."""
        return Usuario.query.all()

    def update(self, user_id: int, **kwargs) -> Usuario:
        """Update user information."""
        usuario = Usuario.query.get_or_404(user_id)

        # Only allow updating specific fields
        allowed_fields = {"password", "rol"}
        for field, value in kwargs.items():
            if field in allowed_fields:
                if field == "password":
                    usuario.set_password(value)
                else:
                    setattr(usuario, field, value)

        db.session.commit()
        return usuario

    def delete(self, user_id: int) -> bool:
        """Delete a user."""
        usuario = Usuario.query.get_or_404(user_id)
        db.session.delete(usuario)
        db.session.commit()
        return True

    def change_password(self, user_id: int, old_password: str, new_password: str) -> bool:
        """Change user password."""
        usuario = Usuario.query.get_or_404(user_id)

        if not usuario.check_password(old_password):
            raise ValueError("Contraseña antigua incorrecta")

        if not new_password or len(new_password) < 6:
            raise ValueError("Nueva contraseña debe tener al menos 6 caracteres")

        usuario.set_password(new_password)
        db.session.commit()
        return True

    def is_admin(self, user_id: int) -> bool:
        """Check if user is admin."""
        usuario = Usuario.query.get(user_id)
        return usuario and usuario.is_admin()

"""Usuario model."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db


class Usuario(UserMixin, db.Model):
    """Usuario model for authentication and authorization."""

    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    rol = db.Column(
        db.String(20),
        nullable=False,
        default="usuario",
        index=True,
    )

    # Relationships
    reservas = db.relationship(
        "Reserva",
        backref="usuario_rel",
        lazy="dynamic",
        cascade="all, delete-orphan",
    )

    def set_password(self, password: str) -> None:
        """Hash and set the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verify the password."""
        return check_password_hash(self.password_hash, password)

    def is_admin(self) -> bool:
        """Check if user is admin."""
        return self.rol == "admin"

    @property
    def cant_reservas(self) -> int:
        """Get count of user reservations."""
        return self.reservas.count()

    def __repr__(self) -> str:
        return f"<Usuario {self.username}>"

"""Reserva model."""
from datetime import datetime

from app.extensions import db


class Reserva(db.Model):
    """Reserva model for trip reservations."""

    __tablename__ = "reserva"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, index=True)
    email = db.Column(db.String(120), nullable=False, index=True)
    fecha = db.Column(db.String(20), nullable=False)
    mensaje = db.Column(db.Text, nullable=True)
    creada_en = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Foreign keys
    viaje_id = db.Column(
        db.Integer,
        db.ForeignKey("viaje.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "fecha": self.fecha,
            "mensaje": self.mensaje,
            "viaje_id": self.viaje_id,
            "usuario_id": self.usuario_id,
            "creada_en": self.creada_en.isoformat() if self.creada_en else None,
        }

    def __repr__(self) -> str:
        return f"<Reserva {self.nombre} - Viaje {self.viaje_id}>"

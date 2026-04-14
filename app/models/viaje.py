"""Viaje model."""
from decimal import Decimal

from app.extensions import db


class Viaje(db.Model):
    """Viaje model for travel packages."""

    __tablename__ = "viaje"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, index=True)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.String(20), nullable=True, index=True)
    precio = db.Column(db.Numeric(10, 2), nullable=True)
    imagen = db.Column(db.String(200), nullable=True)

    # Relationships
    reservas = db.relationship(
        "Reserva",
        backref="viaje_rel",
        lazy="dynamic",
        cascade="all, delete-orphan",
    )

    @property
    def precio_float(self) -> float:
        """Get price as float."""
        return float(self.precio) if self.precio else 0.0

    @property
    def reservas_count(self) -> int:
        """Get count of reservations for this trip."""
        return self.reservas.count()

    def __repr__(self) -> str:
        return f"<Viaje {self.nombre}>"

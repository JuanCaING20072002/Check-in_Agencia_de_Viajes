"""Reservation (reserva) service."""

from typing import List, Optional

from app.extensions import db
from app.models import Reserva, Viaje
from app.services.base_service import BaseService


class ReservaService(BaseService):
    """Service for reservation operations."""

    def create(
        self,
        nombre: str,
        email: str,
        viaje_id: int,
        fecha: Optional[str] = None,
        mensaje: Optional[str] = None,
        usuario_id: Optional[int] = None,
    ) -> Reserva:
        """Create a new reservation."""
        self._validate_required_fields(
            {"nombre": nombre, "email": email, "viaje_id": viaje_id},
            ["nombre", "email", "viaje_id"],
        )

        # Verify viaje exists
        viaje = Viaje.query.get_or_404(viaje_id)

        reserva = Reserva(
            nombre=nombre,
            email=email,
            fecha=fecha or "",
            mensaje=mensaje or "",
            viaje_id=viaje_id,
            usuario_id=usuario_id,
        )

        db.session.add(reserva)
        db.session.commit()

        return reserva

    def get_by_id(self, reserva_id: int) -> Optional[Reserva]:
        """Get reservation by ID."""
        return Reserva.query.get(reserva_id)

    def get_all(self) -> List[Reserva]:
        """Get all reservations."""
        return Reserva.query.all()

    def get_by_viaje(self, viaje_id: int) -> List[Reserva]:
        """Get all reservations for a specific viaje."""
        return Reserva.query.filter_by(viaje_id=viaje_id).all()

    def get_by_usuario(self, usuario_id: int) -> List[Reserva]:
        """Get all reservations for a specific user."""
        return Reserva.query.filter_by(usuario_id=usuario_id).all()

    def get_by_email(self, email: str) -> List[Reserva]:
        """Get all reservations by email."""
        return Reserva.query.filter_by(email=email).all()

    def update(self, reserva_id: int, **kwargs) -> Reserva:
        """Update reservation information."""
        reserva = Reserva.query.get_or_404(reserva_id)

        allowed_fields = {"nombre", "email", "fecha", "mensaje"}
        for field, value in kwargs.items():
            if field in allowed_fields:
                setattr(reserva, field, value)

        db.session.commit()
        return reserva

    def delete(self, reserva_id: int) -> bool:
        """Delete a reservation."""
        reserva = Reserva.query.get_or_404(reserva_id)
        db.session.delete(reserva)
        db.session.commit()
        return True

    def get_reservas_by_email(self, email: str) -> List[Reserva]:
        """Get all reservations by email with viaje info."""
        return Reserva.query.filter_by(email=email).all()

    def get_reservas_count_by_viaje(self, viaje_id: int) -> int:
        """Get count of reservations for a viaje."""
        return Reserva.query.filter_by(viaje_id=viaje_id).count()

    def get_reservas_count_by_usuario(self, usuario_id: int) -> int:
        """Get count of reservations for a user."""
        return Reserva.query.filter_by(usuario_id=usuario_id).count()

    def cancel_reservation(self, reserva_id: int) -> bool:
        """Cancel (delete) a reservation."""
        return self.delete(reserva_id)

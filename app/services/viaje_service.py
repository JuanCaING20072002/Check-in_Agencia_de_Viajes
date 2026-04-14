"""Travel (viaje) service."""

from decimal import Decimal
from typing import List, Optional

from app.extensions import db
from app.models import Viaje
from app.services.base_service import BaseService


class ViajeService(BaseService):
    """Service for travel (viaje) operations."""

    def create(
        self,
        nombre: str,
        descripcion: str,
        fecha: Optional[str] = None,
        precio: Optional[Decimal] = None,
        imagen: Optional[str] = None,
    ) -> Viaje:
        """Create a new travel package."""
        self._validate_required_fields(
            {"nombre": nombre, "descripcion": descripcion},
            ["nombre", "descripcion"],
        )

        viaje = Viaje(
            nombre=nombre,
            descripcion=descripcion,
            fecha=fecha,
            precio=price if (price := Decimal(str(precio)) if precio else None) else None,
            imagen=imagen,
        )

        db.session.add(viaje)
        db.session.commit()

        return viaje

    def get_by_id(self, viaje_id: int) -> Optional[Viaje]:
        """Get travel by ID."""
        return Viaje.query.get(viaje_id)

    def get_all(self) -> List[Viaje]:
        """Get all travels."""
        return Viaje.query.all()

    def get_by_fecha(self, fecha: str) -> List[Viaje]:
        """Get travels by date."""
        return Viaje.query.filter_by(fecha=fecha).all()

    def get_by_price_range(self, min_price: Decimal, max_price: Decimal) -> List[Viaje]:
        """Get travels within price range."""
        return Viaje.query.filter(Viaje.precio >= min_price, Viaje.precio <= max_price).all()

    def update(self, viaje_id: int, **kwargs) -> Viaje:
        """Update travel information."""
        viaje = Viaje.query.get_or_404(viaje_id)

        allowed_fields = {"nombre", "descripcion", "fecha", "precio", "imagen"}
        for field, value in kwargs.items():
            if field in allowed_fields:
                if field == "precio" and value:
                    value = Decimal(str(value))
                setattr(viaje, field, value)

        db.session.commit()
        return viaje

    def delete(self, viaje_id: int) -> bool:
        """Delete a travel."""
        viaje = Viaje.query.get_or_404(viaje_id)
        db.session.delete(viaje)
        db.session.commit()
        return True

    def get_reservas(self, viaje_id: int) -> List:
        """Get all reservations for a travel."""
        viaje = Viaje.query.get_or_404(viaje_id)
        return viaje.reservas.all()

    def get_reservas_count(self, viaje_id: int) -> int:
        """Get count of reservations for a travel."""
        viaje = Viaje.query.get_or_404(viaje_id)
        return viaje.reservas.count()

    def search(self, query: str) -> List[Viaje]:
        """Search travels by name or description."""
        return Viaje.query.filter(
            (Viaje.nombre.ilike(f"%{query}%")) | (Viaje.descripcion.ilike(f"%{query}%"))
        ).all()

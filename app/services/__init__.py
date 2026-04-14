"""Services module - business logic layer."""

from app.services.auth_service import AuthService
from app.services.email_service import EmailService
from app.services.reserva_service import ReservaService
from app.services.viaje_service import ViajeService

# Singleton instances
auth_service = AuthService()
viaje_service = ViajeService()
reserva_service = ReservaService()
email_service = EmailService()

__all__ = [
    "AuthService",
    "ViajeService",
    "ReservaService",
    "EmailService",
    "auth_service",
    "viaje_service",
    "reserva_service",
    "email_service",
]

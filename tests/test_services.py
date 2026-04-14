"""Unit tests for services layer."""

import pytest

from app.models import Reserva, Usuario, Viaje
from app.services import (
    auth_service,
    email_service,
    reserva_service,
    viaje_service,
)


class TestAuthService:
    """Tests for AuthService."""

    def test_create_user(self, db):
        """Test creating a new user."""
        usuario = auth_service.create("testuser", "password123")

        assert usuario.username == "testuser"
        assert usuario.check_password("password123")
        assert not usuario.is_admin()

    def test_create_duplicate_user_raises_error(self, db):
        """Test that creating duplicate user raises error."""
        auth_service.create("testuser", "password123")

        with pytest.raises(ValueError, match="ya existe"):
            auth_service.create("testuser", "otherpass")

    def test_login_valid_credentials(self, db):
        """Test login with valid credentials."""
        auth_service.create("testuser", "password123")
        usuario = auth_service.login("testuser", "password123")

        assert usuario is not None
        assert usuario.username == "testuser"

    def test_login_invalid_credentials(self, db):
        """Test login with invalid credentials."""
        auth_service.create("testuser", "password123")
        usuario = auth_service.login("testuser", "wrongpassword")

        assert usuario is None

    def test_login_nonexistent_user(self, db):
        """Test login with non-existent user."""
        usuario = auth_service.login("nonexistent", "password123")

        assert usuario is None

    def test_get_by_username(self, db):
        """Test getting user by username."""
        auth_service.create("testuser", "password123")
        usuario = auth_service.get_by_username("testuser")

        assert usuario is not None
        assert usuario.username == "testuser"

    def test_change_password(self, db):
        """Test changing user password."""
        usuario = auth_service.create("testuser", "oldpassword")

        auth_service.change_password(usuario.id, "oldpassword", "newpassword")

        # Verify old password doesn't work
        assert auth_service.login("testuser", "oldpassword") is None

        # Verify new password works
        assert auth_service.login("testuser", "newpassword") is not None


class TestViajeService:
    """Tests for ViajeService."""

    @pytest.fixture
    def sample_viaje(self, db):
        """Create a sample travel package."""
        viaje = Viaje(
            nombre="Viaje a Cartagena",
            descripcion="Hermoso viaje al Caribe",
            fecha="2024-06-15",
            precio="500.00",
            imagen=None,
        )
        db.session.add(viaje)
        db.session.commit()
        return viaje

    def test_create_viaje(self, db):
        """Test creating a travel package."""
        viaje = viaje_service.create(
            nombre="Viaje a Santa Marta",
            descripcion="Aventura en la Sierra Nevada",
            fecha="2024-07-01",
            precio="600.00",
            imagen=None,
        )

        assert viaje.nombre == "Viaje a Santa Marta"
        assert viaje.descripcion == "Aventura en la Sierra Nevada"

    def test_get_viaje_by_id(self, db, sample_viaje):
        """Test getting a travel package by ID."""
        viaje = viaje_service.get_by_id(sample_viaje.id)

        assert viaje is not None
        assert viaje.nombre == "Viaje a Cartagena"

    def test_get_all_viajes(self, db, sample_viaje):
        """Test getting all travel packages."""
        viajes = viaje_service.get_all()

        assert len(viajes) >= 1
        assert sample_viaje in viajes

    def test_search_viajes(self, db, sample_viaje):
        """Test searching travel packages."""
        viajes = viaje_service.search("Cartagena")

        assert len(viajes) >= 1
        assert sample_viaje in viajes


class TestReservaService:
    """Tests for ReservaService."""

    @pytest.fixture
    def setup_data(self, db):
        """Setup sample data for tests."""
        viaje = Viaje(
            nombre="Viaje a Bogotá",
            descripcion="Capital del país",
            fecha="2024-08-01",
            precio="400.00",
            imagen=None,
        )
        usuario = Usuario(username="traveler")
        usuario.set_password("password123")

        db.session.add(viaje)
        db.session.add(usuario)
        db.session.commit()

        return {"viaje": viaje, "usuario": usuario}

    def test_create_reserva(self, db, setup_data):
        """Test creating a reservation."""
        reserva = reserva_service.create(
            nombre="Juan Pérez",
            email="juan@example.com",
            fecha="2024-08-01",
            mensaje="Quiero reservar este viaje",
            viaje_id=setup_data["viaje"].id,
        )

        assert reserva.nombre == "Juan Pérez"
        assert reserva.email == "juan@example.com"
        assert reserva.viaje_id == setup_data["viaje"].id

    def test_get_reserva_by_id(self, db, setup_data):
        """Test getting a reservation by ID."""
        reserva = reserva_service.create(
            nombre="María García",
            email="maria@example.com",
            fecha="2024-08-01",
            mensaje="",
            viaje_id=setup_data["viaje"].id,
        )

        fetched = reserva_service.get_by_id(reserva.id)

        assert fetched is not None
        assert fetched.nombre == "María García"

    def test_get_reservas_by_viaje(self, db, setup_data):
        """Test getting reservations by travel package."""
        reserva1 = reserva_service.create(
            nombre="Person 1",
            email="person1@example.com",
            fecha="2024-08-01",
            mensaje="",
            viaje_id=setup_data["viaje"].id,
        )

        reserva2 = reserva_service.create(
            nombre="Person 2",
            email="person2@example.com",
            fecha="2024-08-01",
            mensaje="",
            viaje_id=setup_data["viaje"].id,
        )

        reservas = reserva_service.get_by_viaje(setup_data["viaje"].id)

        assert len(reservas) >= 2
        assert reserva1 in reservas
        assert reserva2 in reservas

    def test_get_reservas_by_email(self, db, setup_data):
        """Test getting reservations by email."""
        reserva = reserva_service.create(
            nombre="Contact",
            email="contact@example.com",
            fecha="2024-08-01",
            mensaje="",
            viaje_id=setup_data["viaje"].id,
        )

        reservas = reserva_service.get_by_email("contact@example.com")

        assert len(reservas) >= 1
        assert reserva in reservas

    def test_cancel_reservation(self, db, setup_data):
        """Test canceling a reservation."""
        reserva = reserva_service.create(
            nombre="To Cancel",
            email="cancel@example.com",
            fecha="2024-08-01",
            mensaje="",
            viaje_id=setup_data["viaje"].id,
        )

        original_id = reserva.id
        reserva_service.delete(reserva.id)

        # Should not find after deletion
        fetched = reserva_service.get_by_id(original_id)
        assert fetched is None


class TestEmailService:
    """Tests for EmailService."""

    def test_is_configured(self):
        """Test email service configuration check."""
        # This might be False in test environment
        is_configured = email_service.is_configured()
        # Just verify it returns a boolean
        assert isinstance(is_configured, bool)

    def test_send_email_method_exists(self):
        """Test that send_email method exists."""
        assert hasattr(email_service, "send_email")
        assert callable(email_service.send_email)

    def test_send_welcome_email_method_exists(self):
        """Test that send_welcome_email method exists."""
        assert hasattr(email_service, "send_welcome_email")
        assert callable(email_service.send_welcome_email)

    def test_send_reset_password_email_method_exists(self):
        """Test that send_reset_password_email method exists."""
        assert hasattr(email_service, "send_reset_password_email")
        assert callable(email_service.send_reset_password_email)

    def test_send_reservation_confirmation_method_exists(self):
        """Test that send_reservation_confirmation method exists."""
        assert hasattr(email_service, "send_reservation_confirmation")
        assert callable(email_service.send_reservation_confirmation)

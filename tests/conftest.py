"""Pytest configuration and fixtures."""
import os

import pytest

from app import create_app
from app.extensions import db as database
from app.models import Reserva, Usuario, Viaje


@pytest.fixture(scope="session")
def app():
    """Create application for the tests."""
    app = create_app("testing")
    
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope="function")
def runner(app):
    """A test runner for the app's CLI commands."""
    return app.test_cli_runner()


@pytest.fixture(scope="function")
def db(app):
    """Create a clean database for each test."""
    with app.app_context():
        database.create_all()
        yield database
        database.session.remove()
        database.drop_all()


@pytest.fixture(scope="function")
def auth_client(client, app):
    """A test client logged in as a regular user."""
    with app.app_context():
        usuario = Usuario(username="testuser")
        usuario.set_password("testpass123")
        database.session.add(usuario)
        database.session.commit()
    
    client.post(
        "/auth/login",
        data={"username": "testuser", "password": "testpass123"},
    )
    return client


@pytest.fixture(scope="function")
def admin_client(client, app):
    """A test client logged in as an admin user."""
    with app.app_context():
        usuario = Usuario(username="admin", rol="admin")
        usuario.set_password("adminpass123")
        database.session.add(usuario)
        database.session.commit()
    
    client.post(
        "/auth/login",
        data={"username": "admin", "password": "adminpass123"},
    )
    return client


@pytest.fixture(scope="function")
def sample_viaje(db):
    """Create a sample trip for testing."""
    viaje = Viaje(
        nombre="Viaje a Bogotá",
        descripcion="Un hermoso viaje a la capital",
        fecha="2024-05-01",
        precio=500000,
        imagen="bogota.jpg",
    )
    db.session.add(viaje)
    db.session.commit()
    return viaje


@pytest.fixture(scope="function")
def sample_reserva(db, sample_viaje):
    """Create a sample reservation for testing."""
    reserva = Reserva(
        nombre="Juan Pérez",
        email="juan@example.com",
        fecha="2024-04-15",
        mensaje="Quiero reservar este viaje",
        viaje_id=sample_viaje.id,
    )
    db.session.add(reserva)
    db.session.commit()
    return reserva

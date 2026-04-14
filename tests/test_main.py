"""Test main routes."""
import pytest


@pytest.mark.unit
def test_health(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


@pytest.mark.unit
def test_index(client):
    """Test home page."""
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.unit
def test_viajes_listar(client):
    """Test list viajes page."""
    response = client.get("/viajes/")
    assert response.status_code == 200


@pytest.mark.unit
def test_login_page(client):
    """Test login page loads."""
    response = client.get("/auth/login")
    assert response.status_code == 200


@pytest.mark.unit
def test_register_page(client):
    """Test register page loads."""
    response = client.get("/auth/register")
    assert response.status_code == 200

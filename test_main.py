import pytest
from farm.main import app

# testing if all the paths work


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_cow(client):
    response = client.get("/cow")
    assert response.status_code == 200


def test_dog(client):
    response = client.get("/dog")
    assert response.status_code == 200


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302

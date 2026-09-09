from apps.app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_version():
    response = client.get("/version")
    assert response.status_code == 200


def test_info():
    response = client.get("/info")
    assert response.status_code == 200

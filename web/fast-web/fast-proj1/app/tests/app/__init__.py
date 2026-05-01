from fastapi import status
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_redirect_to_home():
    try:
        response = client.get("/")
        assert (
            response.status_code == status.HTTP_200_OK
            or status.HTTP_307_TEMPORARY_REDIRECT
        )
        assert response.json() == {"message": "home page"}
    except AssertionError as e:
        raise e
    finally:
        client.close()

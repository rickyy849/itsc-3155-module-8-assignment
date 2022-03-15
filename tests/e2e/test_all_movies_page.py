# TODO: Feature 1
import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()

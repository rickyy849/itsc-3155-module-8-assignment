# TODO: Feature 3
from flask.testing import FlaskClient
from app import app

def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search/?movie-title=Good-Test')
    response_data = response.data;
    assert 3 in response_data;

    response = test_app.get('/movies/search/?movie-title=Bad-Test')
    response_data = response.data;
    assert "No such movie in database" in response_data;
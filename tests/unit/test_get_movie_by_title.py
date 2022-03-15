# TODO: Feature 3
from src.repositories.movie_repository import movie_repository_singleton

def search(title):
    movie = movie_repository_singleton.get_movie_by_title(title);
    if (movie != None):
        return movie.rating;
    else:
        return -1;

def test_get_movie_by_title():
    movie_repository_singleton.create_movie('Good-Test', 'Hi', 3);
    movie_repository_singleton.create_movie('Another Test', 'Hello', 2);

    assert search('Good-Test') == 3;
    assert search('Bad Test') == -1;


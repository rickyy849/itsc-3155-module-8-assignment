# TODO: Feature 2
from src.models.movie import Movie

def test_create_movie():
    usermovie = input()
    str(usermovie)
    userdirector = input()
    str(userdirector)
    userrating = input()
    int(userrating)

    movie = Movie(usermovie,userdirector,userrating)

    assert movie.title == usermovie
    assert movie.director == userdirector
    assert movie.rating == userrating
    assert movie.rating > 0
    assert movie.rating < 6
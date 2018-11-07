from flask import render_template

from models.book.book import Book
from models.magazine.magazine import Magazine
from models.music.music import Music
from models.movie.movie import Movie


def view_catalog(db_gateway, request):
    books = db_gateway.get_all(Book, 'books')
    magazines = db_gateway.get_all(Magazine, 'magazines')
    musics = db_gateway.get_all(Music, 'musics')
    movies = db_gateway.get_all(Movie, 'movies')

    return render_template('catalog.html', books=books, magazines=magazines, musics=musics, movies=movies)

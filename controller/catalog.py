from flask import render_template

from models.book.book import Book
from models.magazine.magazine import Magazine
from models.music.music import Music
from models.movie.movie import Movie

class Catalog():
    
    @staticmethod
    def view_catalog(db_gateway, request):
        books = db_gateway.get_all(Book)
        magazines = db_gateway.get_all(Magazine)
        musics = db_gateway.get_all(Music)
        movies = db_gateway.get_all(Movie)

        return render_template('user_dashboard.html', books=books, magazines=magazines, musics=musics, movies=movies)

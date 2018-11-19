from flask import render_template

from models.book import Book
from models.magazine import Magazine
from models.music import Music
from models.movie import Movie

class Catalog():
    
    @staticmethod
    def view_catalog(db_gateway, request):
        books = db_gateway.get_all(Book)
        magazines = db_gateway.get_all(Magazine)
        musics = db_gateway.get_all(Music)
        movies = db_gateway.get_all(Movie)

        return render_template('catalog.html', books=books, magazines=magazines, musics=musics, movies=movies, is_admin=db_gateway.verify_admin(request.cookies.get('username')))

        

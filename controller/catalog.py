from flask import render_template

from models import Book
from models import Magazine
from models import Music
from models import Movie

class Catalog():
    
    @staticmethod
    def view_catalog(db_gateway, request):
        books = db_gateway.get_all(Book)
        magazines = db_gateway.get_all(Magazine)
        musics = db_gateway.get_all(Music)
        movies = db_gateway.get_all(Movie)

        return render_template('catalog.html', books=books, magazines=magazines, musics=musics, movies=movies, is_admin=db_gateway.verify_admin(request.cookies.get('username')))

        

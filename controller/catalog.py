from flask import render_template, request

from controller.controller import Controller
from models.book import Book
from models.magazine import Magazine
from models.music import Music
from models.movie import Movie


class Catalog(Controller):
    def view_catalog(self):
        books = self.db.get_all(Book)
        magazines = self.db.get_all(Magazine)
        musics = self.db.get_all(Music)
        movies = self.db.get_all(Movie)

        return render_template('catalog.html', books=books, magazines=magazines, musics=musics, movies=movies,
                               is_admin=self.db.verify_admin(request.cookies.get('username')))

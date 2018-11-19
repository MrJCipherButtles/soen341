from flask import request, render_template
import datetime

from controller.controller import Controller
from models.book import Book
from models.movie import Movie
from models.music import Music
from models.magazine import Magazine


class Loan(Controller):
    def loan_item(self):
        user = request.cookies.get('username')
        itemID = request.form['itemID']
        success = 1 if self.db.loan_item(user, itemID) else 2
        return render_template('loan_cart.html', success=success)

    def view_active_loans(self):
        email = request.cookies.get('username')
        books = self.db.get_all(Book, email)
        musics = self.db.get_all(Music, email)
        movies = self.db.get_all(Movie, email)
        magazines = self.db.get_all(Magazine, email)
        return render_template('active_loans.html', books=books, musics=musics, movies=movies, magazines=magazines)

    def return_item(self):
        self.db.process_return(request.form['id'])

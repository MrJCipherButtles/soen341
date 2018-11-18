from flask import request, render_template
import datetime

from models.book import Book
from models.movie import Movie
from models.music import Music
from models.magazine import Magazine


class Loan:
    @staticmethod
    def loan_item(db_gateway):
        user = request.cookies.get('username')
        itemID = request.form['itemID']
        success = 1 if db_gateway.loan_item(user, itemID) else 2
        return render_template('loan_cart.html', success=success)


    @staticmethod
    def view_active_loans(request, db_gateway):
        email = request.cookies.get('username')
        books = db_gateway.get_all(Book, email)
        musics = db_gateway.get_all(Music, email)
        movies = db_gateway.get_all(Movie, email)
        magazines = db_gateway.get_all(Magazine, email)
        return render_template('active_loans.html', books=books, musics=musics, movies=movies, magazines=magazines)

    @staticmethod
    def return_item(request, db_gateway):
        db_gateway.process_return(request.form['id'])

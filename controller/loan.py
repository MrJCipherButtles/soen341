from flask import request, render_template
import datetime

from models.book.book import Book
from models.movie.movie import Movie
from models.music.music import Music
from models.magazine.magazine import Magazine

class Loan:
    @staticmethod
    def loan_item(db_gateway):
        user = request.cookies.get('username')
        itemID = request.form['itemID']
        db_gateway.cursor.execute(
            "INSERT INTO library.loans (clientId, itemId, loan_date) VALUES ('%s', '%s', '%s')" % (
                user, itemID, datetime.datetime.today().strftime('%Y-%m-%d')))
        db_gateway.conn.commit()
        return "loan successful"

    @staticmethod
    def view_active_loans(request, db_gateway):
        email = request.cookies.get('username')
        books = db_gateway.get_all(Book, email)
        musics = db_gateway.get_all(Music, email)
        movies = db_gateway.get_all(Movie, email)
        magazines = db_gateway.get_all(Magazine, email)
        return render_template('active_loans.html', books=books, musics=musics, movies=movies, magazines = magazines)

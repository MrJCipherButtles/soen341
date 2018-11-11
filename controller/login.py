from flask import render_template, url_for, redirect
from models.book.book import Book


class Login:
    @staticmethod
    def verify_login(db_gateway, request):
        fname = request.form['user']
        lname = request.form['psw']
        # TODO: Include raw sql inside db_gateway
        db_gateway.cursor.execute(
            "SELECT * FROM library.users WHERE firstName = '%s' AND lastName = '%s'" % (fname, lname))
        db_gateway.cursor.fetchall()
        if db_gateway.cursor.rowcount == 0:
            return "Does not exist"
        return redirect(url_for('dashboard'))

    @staticmethod
    def show_login_page():
        return render_template('login.html')

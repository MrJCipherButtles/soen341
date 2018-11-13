from flask import render_template, url_for, redirect, session, make_response
from models.book.book import Book


class Login:
    @staticmethod
    def verify_login(db_gateway, request=None, user=None, pswd=None):
        user = request.form['user']
        pswd = request.form['psw']
        if not db_gateway.verify_login(user, pswd):
            return "Does not exist"
<<<<<<< HEAD
        return redirect(url_for('view_catalog'))
=======
        session['username'] = user
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('username', user)
        return resp
>>>>>>> 3358e3edbfb3d9a95e753fa6ce43a2fce21f903c

    @staticmethod
    def show_login_page():
        return render_template('login.html')

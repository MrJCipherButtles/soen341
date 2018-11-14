from flask import render_template, url_for, redirect, session, make_response
from models.book.book import Book


class Login:
    @staticmethod
    def verify_login(db_gateway, request=None, user=None, pswd=None):
        user = request.form['user']
        pswd = request.form['psw']
        if not db_gateway.verify_login(user, pswd):
            return "Does not exist"
        session['username'] = user
        
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('username', user)
        return resp

    @staticmethod
    def show_login_page():
        return render_template('login.html')

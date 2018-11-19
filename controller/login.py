from flask import render_template, url_for, redirect, session, make_response, request

from controller.controller import Controller


class Login(Controller):
    active_users = 0

    def verify_login(self):
        user = request.form['user']
        pswd = request.form['psw']
        if not self.db.verify_login(user, pswd):
            return "Does not exist"
        session['username'] = user
        
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('username', user)
        Login.active_users += 1
        print(Login.active_users)
        return resp

    def logout(self):
        resp = make_response(redirect(url_for('login')))
        resp.delete_cookie('username')
        session.pop('username', None)
        Login.active_users -= 1
        print(Login.active_users)
        return resp

    def show_login_page(self, has_account_error=False):
        return render_template('login.html', err=has_account_error)

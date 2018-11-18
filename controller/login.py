from flask import render_template, url_for, redirect, session, make_response


class Login:
    active_users = 0

    @staticmethod
    def verify_login(db_gateway, request=None, user=None, pswd=None):
        user = request.form['user']
        pswd = request.form['psw']
        if not db_gateway.verify_login(user, pswd):
            return "Does not exist"
        session['username'] = user
        
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('username', user)
        Login.active_users += 1
        print(Login.active_users)
        return resp

    @staticmethod
    def logout():
        resp = make_response(redirect(url_for('login')))
        resp.delete_cookie('username')
        session.pop('username', None)
        Login.active_users -= 1
        print(Login.active_users)
        return resp

    @staticmethod
    def show_login_page(has_account_error=False):
        return render_template('login.html', has_account_error=has_account_error)

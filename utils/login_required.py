from functools import wraps

from flask import session, flash, redirect, url_for, request


class LoginValidator:
    @staticmethod
    def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            user = request.cookies.get('username')
            if user is not None:
                return f(*args, **kwargs)
            else:
                flash("You need to login first")
                return redirect(url_for('login'))

        return wrap

    @staticmethod
    def admin(db_gateway, denied=False):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                user = request.cookies.get('username')
                if user is None:
                    return redirect(url_for('restricted'))
                if not denied == db_gateway.verify_admin(user):
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('restricted'))

            return wrapper
        return decorator
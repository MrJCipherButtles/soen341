from functools import wraps

from flask import session, flash, redirect, url_for, request


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


def admin_required(db_gateway):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = request.cookies.get('username')
            if user is None:
                return redirect(url_for('restricted'))
            if db_gateway.verify_admin(user):
                return f(*args, **kwargs)
            else:
                return redirect(url_for('restricted'))

        return wrapper
    return decorator
from flask import Flask, render_template, request
from db_connection import DBGateway
from views.login import show_login_page, verify_login
from views.register import register_user

app = Flask(__name__)
db_gateway = DBGateway(app)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return show_login_page()
    else:
        return verify_login(db_gateway, request)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return register_user(db_gateway, request)


if __name__ == "__main__":
    app.run()

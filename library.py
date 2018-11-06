from flask import Flask, render_template, request
from db_connection import DBGateway
from views.login import Login
from views.register import Register

app = Flask(__name__)
db_gateway = DBGateway(app)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return Login.show_login_page()
    elif request.method == 'POST':
        return Login.verify_login(db_gateway, request)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        return Register.register_user(db_gateway, request)


if __name__ == "__main__":
    app.run()

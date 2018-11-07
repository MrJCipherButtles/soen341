from flask import Flask, render_template, request, url_for, redirect
from utils.login_required import login_required
from db_connection import DBGateway
from controller.login import Login
from controller.register import Register
from controller.catalog import view_catalog

app = Flask(__name__)
db_gateway = DBGateway(app)


@app.route('/')
def _():
    return redirect(url_for('login'))


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


# @app.route("/dashboard/<firstname>_<lastname>", methods=['GET','POST'])
# def dashboard(firstname, lastname):
#     if request.method == 'GET':
#         return render_template('dashboard.html',())
#     elif request.method == 'POST':


# @app.route("/catalog")
# # @login_required
# def catalog():
#     return view_catalog(db_gateway, request)


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, url_for, redirect, session, make_response

from utils.login_required import login_required, admin_required
from db_connection import DBGateway
from controller.login import Login
from controller.register import Register
from controller.process_item import ProcessItem
from controller.catalog import Catalog

app = Flask(__name__)
app.secret_key = b'\xfb\xcf\x9e\x10\xd2\xdc2\x86\xe3\xf8\xf6\xf1\x89\xe1\xf8R'
db_gateway = DBGateway(app)
app.template_folder = 'view/templates'
app.static_folder = 'view/static'


@app.route('/')
@login_required
def index():
    return redirect(url_for('dashboard'))


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


@app.route("/add_item", methods=['GET', 'POST'])
@admin_required(db_gateway)
def add_item():
    if (request.method == 'POST'):
        ProcessItem.add(request, db_gateway)
    return render_template('add_item.html')


@app.route("/delete_item", methods=['GET', 'POST'])
@admin_required(db_gateway)
def delete_item():
    if request.method == 'POST':
        return ProcessItem.remove(request, db_gateway)
    return render_template('delete_item.html')


@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        return Catalog.view_catalog(db_gateway, request)
    elif request.method == 'POST':
        return None


@app.route("/logout")
@login_required
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('username')
    session.pop('username', None)
    print(request.cookies.get('username'))
    return resp


# @app.route("/catalog")
# # @login_required
# def catalog():
#     return view_catalog(db_gateway, request)


if __name__ == "__main__":
    app.run()

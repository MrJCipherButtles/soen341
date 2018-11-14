from flask import Flask, render_template, request, url_for, redirect, session, make_response

from models.book.book import Book
from models.movie.movie import Movie
from models.music.music import Music
from utils.login_required import login_required, admin
from db_connection import DBGateway
from controller.login import Login
from controller.register import Register
from controller.process_item import ProcessItem
from controller.catalog import Catalog
from controller.loan import Loan

app = Flask(__name__)
app.secret_key = b'\xfb\xcf\x9e\x10\xd2\xdc2\x86\xe3\xf8\xf6\xf1\x89\xe1\xf8R'
db_gateway = DBGateway(app)
app.template_folder = 'view/templates'
app.static_folder = 'view/static'

app.active_users = 0


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
@login_required
def index(path):
    return redirect(url_for('home'))


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


@app.route("/registerAdmin", methods=['GET', 'POST'])
@admin(db_gateway)
def registeradmin():
    if request.method == 'GET':
        return render_template('registerAdmin.html')
    elif request.method == 'POST':
        return Register.register_user_admin(db_gateway, request)


@app.route("/successLogin", methods=['GET'])
def successLogin():
    if request.method == 'GET':
        return render_template('successLogin.html')
    elif not (request.method == 'GET'):
        return "Illegal action"


@app.route("/add_item", methods=['GET', 'POST'])
@admin(db_gateway)
def add_item():
    if request.method == 'POST':
        ProcessItem.add(request, db_gateway)
    return render_template('add_item.html')


@app.route("/delete_item", methods=['GET', 'POST'])
@admin(db_gateway)
def delete_item():
    if request.method == 'POST':
        return ProcessItem.remove(request, db_gateway)
    return render_template('delete_item.html')


@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'GET':
    return Catalog.view_catalog(db_gateway, request)
  elif request.method == 'POST':
    return None


@app.route("/logout")
@login_required
def logout():
    return Login.logout()


@app.route("/loan_cart", methods=['GET', 'POST'])
@login_required
@admin(db_gateway, denied=True)
def loan():
    if request.method == 'GET':
        return render_template('loan_cart.html')
    elif request.method == 'POST':
        return Loan.loan_item(db_gateway)


@app.route("/DeleteItem", methods=['GET', 'POST'])
@admin(db_gateway)
def deleteItem():
    if request.method == 'GET':
        return render_template('DeleteItem.html')
    elif request.method == 'POST':
        return ProcessItem.remove(request, db_gateway)


@app.route("/AddItem", methods=['GET', 'POST'])
@admin(db_gateway)
def addItem():
    if request.method == 'GET':
        return render_template('AddItem.html')
    elif request.method == 'POST':
        ProcessItem.add(request, db_gateway)


@app.route("/EditItem", methods=['GET', 'POST'])
@admin(db_gateway)
def editItem():
    if request.method == 'GET':
        return render_template('EditItem.html')
    elif request.method == 'POST':
        return Loan.loan_item(db_gateway, request)


@app.route("/search", methods=['GET', 'POST'])
@login_required
@admin(db_gateway, denied=True)
def search():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        return Loan.loan_item(db_gateway, request)


@app.route("/restricted")
def restricted():
    return render_template('restriction.html')


@app.route("/active_loans")
@login_required
@admin(db_gateway, denied=True)
def active_loans():
    return Loan.view_active_loans(request, db_gateway)


@app.route("/active_users")
@admin(db_gateway)
def active_users():
    return render_template('active_users.html', active_users=Login.active_users)


# @app.route("/catalog")
# # @login_required
# def catalog():
#     return view_catalog(db_gateway, request)


if __name__ == "__main__":
    app.run()

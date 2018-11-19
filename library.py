from flask import Flask, render_template, request, url_for, redirect, make_response
from utils.login_required import LoginValidator
from db_connection import DBGateway
from controller.login import Login
from controller.register import Register
from controller.process_item import ProcessItem
from controller.catalog import Catalog
from controller.loan import Loan
from controller.search import SearchItem

app = Flask(__name__)
app.secret_key = b'\xfb\xcf\x9e\x10\xd2\xdc2\x86\xe3\xf8\xf6\xf1\x89\xe1\xf8R'
db_gateway = DBGateway(app)
app.template_folder = 'view/templates'
app.static_folder = 'view/static'
app.active_users = 0
Login = Login(db_gateway)
Register = Register(db_gateway)
ProcessItem = ProcessItem(db_gateway)
Catalog = Catalog(db_gateway)
Loan = Loan(db_gateway)
SearchItem = SearchItem(db_gateway)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
@LoginValidator.login_required
def index(path):
    return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        try:
            return Login.show_login_page(request.args['err'])
        except:
            return Login.show_login_page(False)
    elif request.method == 'POST':
        return Login.verify_login()


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        try:
            return Register.register_user()
        except:
            return redirect(url_for('login', err=True))


@app.route("/registerAdmin", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def registeradmin():
    if request.method == 'GET':
        return render_template('registerAdmin.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return Register.register_user_admin()


@app.route("/successLogin", methods=['GET'])
def successLogin():
    if request.method == 'GET':
        return render_template('successLogin.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif not (request.method == 'GET'):
        return "Illegal action"





@app.route("/delete_item", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def delete_item():
    if request.method == 'POST':
        return ProcessItem.remove()
    return render_template('DeleteItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))


@app.route("/return_item", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def return_item():
    if request.method == 'POST':
        Loan.return_item()
    return render_template('return_item.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))


@app.route("/home", methods=['GET', 'POST'])
@LoginValidator.login_required
def home():
    return Catalog.view_catalog()


@app.route("/logout")
@LoginValidator.login_required
def logout():
    return Login.logout()


@app.route("/loan_cart", methods=['GET', 'POST'])
@LoginValidator.login_required
@LoginValidator.admin(db_gateway, denied=True)
def loan():
    if request.method == 'GET':
        return render_template('loan_cart.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return Loan.loan_item()



@app.route("/AddItem", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def add_item():
    success = False
    if request.method == 'POST':
        ProcessItem.add()
        success = True
    return render_template('AddItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')), success = success)




@app.route("/DeleteItem", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def deleteItem():

    if request.method == 'GET':
        return render_template('DeleteItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return ProcessItem.remove()


@app.route("/EditItem", methods=['GET', 'POST'])
@LoginValidator.admin(db_gateway)
def editItem():
    if request.method == 'GET':
        return render_template('EditItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return ProcessItem.view_item()

@app.route("/view_edit_item", methods=['GET','POST'])
@LoginValidator.admin(db_gateway)
def view_edit_item():
    if request.method == 'GET':
        return render_template('view_edit_item.html', id=request.args.get('itemId') ,item=db_gateway.get_item_by_id(request.args.get('itemId')), is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return ProcessItem.edit()


@app.route("/search", methods=['GET', 'POST'])
@LoginValidator.login_required
def search():
    if request.method == 'GET':
        return render_template('search.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return SearchItem.searchItem()

@app.route("/restricted")
def restricted():
    return render_template('restriction.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))

@app.route("/active_loans")
@LoginValidator.login_required
@LoginValidator.admin(db_gateway, denied=True)
def active_loans():
    return Loan.view_active_loans()


@app.route("/active_users")
@LoginValidator.admin(db_gateway)
def active_users():
    return render_template('active_users.html', active_users=Login.active_users,
                           is_admin=db_gateway.verify_admin(request.cookies.get('username')))

if __name__ == "__main__":
    app.run(debug=True)

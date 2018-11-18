from flask import Flask, render_template, request, url_for, redirect
from models import Music
from utils.login_required import login_required, admin
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


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
@login_required
def index(path):
    return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return Login.show_login_page(request.args['err'])
    elif request.method == 'POST':
        return Login.verify_login(db_gateway, request)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        try:
            return Register.register_user(db_gateway, request)
        except:
            return redirect(url_for('login', err=True))


@app.route("/registerAdmin", methods=['GET', 'POST'])
@admin(db_gateway)
def registeradmin():
    if request.method == 'GET':
        return render_template('registerAdmin.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return Register.register_user_admin(db_gateway, request)


@app.route("/successLogin", methods=['GET'])
def successLogin():
    if request.method == 'GET':
        return render_template('successLogin.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif not (request.method == 'GET'):
        return "Illegal action"





@app.route("/delete_item", methods=['GET', 'POST'])
@admin(db_gateway)
def delete_item():
    if request.method == 'POST':
        return ProcessItem.remove(request, db_gateway)
    return render_template('DeleteItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))


@app.route("/return_item", methods=['GET', 'POST'])
@admin(db_gateway)
def return_item():
    if request.method == 'POST':
        Loan.return_item(request, db_gateway)
    return render_template('return_item.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))


@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return Catalog.view_catalog(db_gateway, request)




@app.route("/logout")
@login_required
def logout():
    return Login.logout()


@app.route("/loan_cart", methods=['GET', 'POST'])
@login_required
@admin(db_gateway, denied=True)
def loan():
    if request.method == 'GET':
        return render_template('loan_cart.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return Loan.loan_item(db_gateway)



@app.route("/AddItem", methods=['GET', 'POST'])
@admin(db_gateway)
def add_item():
    success = False
    if request.method == 'POST':
        ProcessItem.add(request, db_gateway)
        success = True
    return render_template('AddItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')), success = success)




@app.route("/DeleteItem", methods=['GET', 'POST'])
@admin(db_gateway)
def deleteItem():

    if request.method == 'GET':
        return render_template('DeleteItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':

        return ProcessItem.remove(request, db_gateway)




@app.route("/EditItem", methods=['GET', 'POST'])
@admin(db_gateway)
def editItem():
    if request.method == 'GET':
        return render_template('EditItem.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return render_template('view_edit_item.html', item=db_gateway.get_item_by_id(request.form['id']))

@app.route('/view_edit_item', methods=['GET','POST'])
@admin(db_gateway)
def view_edit_item():
    if request.method == 'GET':
        return render_template('view_edit_item.html')
    elif request.method == 'POST':
        ProcessItem.edit(request, db_gateway)


@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'GET':
        return render_template('search.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))
    elif request.method == 'POST':
        return SearchItem.searchItem(db_gateway,request)

@app.route("/restricted")
def restricted():
    return render_template('restriction.html', is_admin=db_gateway.verify_admin(request.cookies.get('username')))


@app.route("/active_loans")
@login_required
@admin(db_gateway, denied=True)
def active_loans():
    return Loan.view_active_loans(request, db_gateway)


@app.route("/active_users")
@admin(db_gateway)
def active_users():
    return render_template('active_users.html', active_users=Login.active_users,
                           is_admin=db_gateway.verify_admin(request.cookies.get('username')))

if __name__ == "__main__":
    app.run(debug=True)

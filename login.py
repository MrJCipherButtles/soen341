from flask import Flask, render_template, request
from db_config import db_host, db_name, db_password, db_user
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    fname = request.form['user']
    lname = request.form['psw']
    cursor.execute("SELECT * FROM library.clients WHERE firstName = '%s' AND lastName = '%s'" % (fname, lname))
    cursor.fetchall()
    if cursor.rowcount == 0:
      return "Does not exist"
    return "login successful"


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        fname = request.form['firstname']
        lname = request.form['lastname']
        address_1 = request.form['address-1']
        address_2 = request.form['address-2']
        city = request.form['city']
        state = request.form['state']
        postal = request.form['postal']
        country = request.form['country']
        email = request.form['email']
        password = request.form['psw']
        psw_repeat = request.form['psw']
        phone = request.form['phone']

        if password != psw_repeat:
            return "Passwords do not match"
        cursor.execute(
            "INSERT INTO library.clients (firstName, lastName, address, email, phone) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                fname, lname, address_1 + ' ' + address_2 + ' ' + city + ' ' + state + ' ' + postal + ' ' + country,
                email, str(phone)))
        conn.commit()
        return "registration successful"


if __name__ == "__main__":
    app.run()

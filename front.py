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
def hello():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        cursor.execute("SELECT * FROM library.clients WHERE firstName = '%s' AND lastName = '%s'" % (fname, lname))
        cursor.fetchall()
        if cursor.rowcount == 0:
            return "Does not exist"
        return "login successful"


if __name__ == "__main__":
    app.run()

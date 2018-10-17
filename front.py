from flask import Flask, Response, render_template, request
import os.path

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        return fname + lname



if __name__ == "__main__":
    app.run()

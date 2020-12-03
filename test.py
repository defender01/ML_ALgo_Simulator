from flask import Flask, request, redirect, Response
from flask import render_template

import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to Python Flask!"


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


@app.route("/signUpUser", methods=["POST"])
def signUpUser():
    print("reached destination python program")
    user = request.form['username'];
    print(user)
    password = request.form['password'];
    print(password)
    return json.dumps({'status': 'OK', 'user': user, 'pass': password});


if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, render_template
from flask import request

auth = Blueprint('auth', __name__)


@auth.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + "+" + request.form["password"]
    else:
        return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

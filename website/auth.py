from flask import render_template, Blueprint, redirect, url_for, request
from flask_dance.contrib.github import github

auth = Blueprint('auth', __name__)


@auth.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username


@auth.route('/')
def home():
    return render_template('index.html')

# def github_login():
#     if not github.authorized:
#         return redirect(url_for('github.login'))
#     else:
#         account_info = github.get('/user')
#         if account_info.ok:
#             account_info_json = account_info.json()
#             return render_template('index.html')
#
#     return '<h1>Request failed!</h1>'


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

from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)  # generujemy sekretny klucz aplikacji
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '0'  # zezwalamy na polaczenie w lokalnym  !!!!!!!!!!!
    # srodowisku bez https
    github_blueprint = make_github_blueprint(
        client_id="ce4c36482eb8c5865b8a",
        client_secret="0cf6b734d0ed6fe206c26365c91d4dd566d3a8ef",
    )

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(github_blueprint, url_prefix='/login')

    return app


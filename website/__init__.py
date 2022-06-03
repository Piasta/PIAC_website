from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "databse.db"


def create_app():
    app = Flask(__name__)
    # app.secret_key = secrets.token_hex(16)  # generujemy sekretny klucz aplikacji
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # zezwalamy na polaczenie w lokalnym srodowisku bez https
    # github_blueprint = make_github_blueprint(
    #     client_id="ce4c36482eb8c5865b8a", # mój client_id z githuba
    #     client_secret="0cf6b734d0ed6fe206c26365c91d4dd566d3a8ef",
    # )
    app.config['SECRET_KEY'] = 'hjshjhdjah'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # app.register_blueprint(github_blueprint, url_prefix='/login')
    #
    from .models import User, Note

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
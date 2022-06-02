from flask import abort, make_response
import mysql.connector
from flask import Blueprint, render_template, request, flash, jsonify
from .models import Note
from . import db
import json
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


# @views.route('/home')
# def home():
#     return render_template('index.html')


@views.route('/help')
def help():
    return "Help me"


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)


@views.route('/gallery')
def gallery():
    return render_template('gallery.html', user=current_user)


@views.route('/database')
def database():
    mydb = mysql.connector.connect(
        host="localhost",
        database="Guests",
        user="root",
        password="datadata1"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from guests_list")
    record = mycursor.fetchall()
    return str(record)


@views.route('/error_denied')
def error_denied():
    abort(401)


@views.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


@views.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user)
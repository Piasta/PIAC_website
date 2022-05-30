from flask import abort, make_response
from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"



@views.route('/help')
def help():
    return "Help me"


@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/gallery')
def gallery():
    return render_template('gallery.html')


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
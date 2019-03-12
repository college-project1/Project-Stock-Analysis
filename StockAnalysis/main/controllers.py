from flask import Flask,render_template

from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register')
def register():
    return render_template('register.html')

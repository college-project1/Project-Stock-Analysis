from flask import Flask,render_template

from flask import Blueprint
users = Blueprint('users',__name__, template_folder='templates')

@users.route('/udashboard')
def udashboard():
    return render_template('udashboard.html')

@users.route('/usersupdate')
def usersupdate():
    return render_template('usersupdate.html')

@users.route('/myprofile')
def myprofile():
    return render_template('myprofile.html')

@users.route('/ustockdetails')
def ustockdetails():
    return render_template('ustockdetails.html')

@users.route('/ustocks')
def ustocks():
    return render_template('ustocks.html')

@users.route('/utrades')
def utrades():
    return render_template('utrades.html')

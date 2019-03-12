from flask import Flask,render_template

from flask import Blueprint
admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def adashboard():
    return render_template('adashboard.html')

@admin.route('/stocks')
def stocks():
    return render_template('stocks.html')

@admin.route('/stocksupdate')
def stocksupdate():
    return render_template('stocksupdate.html')

@admin.route('/trades')
def trades():
    return render_template('trades.html')

@admin.route('/tradesupdate')
def tradesupdate():
    return render_template('tradesupdate.html')

@admin.route('/users')
def users():
    return render_template('users.html')

@admin.route('/usersupdate')
def usersupdate():
    return render_template('usersupdate.html')

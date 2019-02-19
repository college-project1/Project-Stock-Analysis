from flask import Flask,render_template

app = Flask(__name__)

#js = Bundle ('login.js',output='gen/main.js',filters='jsmin')
#css = Bundle('login.css',output='gen/main.css',filters='cssmin')

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin')
def adashboard():
    return render_template('adashboard.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

@app.route('/stocksupdate')
def stocksupdate():
    return render_template('stocksupdate.html')

@app.route('/trades')
def trades():
    return render_template('trades.html')

@app.route('/tradesupdate')
def tradesupdate():
    return render_template('tradesupdate.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/usersupdate')
def usersupdate():
    return render_template('usersupdate.html')

@app.route('/myprofile')
def myprofile():
    return render_template('myprofile.html')

@app.route('/ustockdetails')
def ustockdetails():
    return render_template('ustockdetails.html')

@app.route('/ustocks')
def ustocks():
    return render_template('ustocks.html')

@app.route('/utrades')
def utrades():
    return render_template('utrades.html')

    
if __name__ == "__main__":
    app.run(debug=True)
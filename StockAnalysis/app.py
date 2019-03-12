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
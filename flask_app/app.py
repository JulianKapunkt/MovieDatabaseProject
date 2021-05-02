
from flask import Flask, request, render_template, url_for, redirect




app = Flask(__name__)

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup", methods= ['POST'])
def signup():
    username = request.form.get('username','None')
    password = request.form.get('password','None')
    email    = request.form.get('email','None')
    return 'successful'


if __name__ == "__main__":
    app.run(debug=True)
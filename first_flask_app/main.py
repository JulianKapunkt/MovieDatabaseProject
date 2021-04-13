
from flask import Flask, request, render_template, url_for, redirect
import csv

users = {'mahdi': '123',
         'julian': '456',
         'richard': '789'}



app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html', title= "Login Page")

@app.route("/login", methods= ['POST'])
def login():
    username = request.form.get('username','None')
    password = request.form.get('password','None')
    if username in users.keys():
        if password == users[username]:
            #send_email()
            return render_template('login_response.html', parameterübergabe = "Success")
        else:
            return render_template('login_response.html', parameterübergabe= "Failed")
    else:
        return render_template('login_response.html', parameterübergabe= "Failed")

app.run()

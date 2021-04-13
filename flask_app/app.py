
from flask import Flask, request, render_template, url_for, redirect
import csv

users = {'mahdi': '123',
         'julian': '456',
         'richard': '789'}



app = Flask(__name__)
@app.route("/")
def index():
    #name = request.args.get('var', 'World')
    #return render_template('index.html', name = name)
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

@app.route("/register", methods = ['GET','POST'])

def register():
    if request.method == "POST":
        movie_name = request.form.get('moviename','None')
        year = request.form.get('year','None')
        try:
            file = open('register_list.csv','a')  # a means append / r means read and w means write
            writer = csv.writer(file)
            writer.writerow((movie_name, year))
            file.close()
        except:
            return "failed"
        return render_template("registered_success.html", title= "Register Successfull")
    elif request.method == "GET":
        return render_template("register_movies.html", titel = "Register new Movie")



@app.route("/registered_movies", methods = ['GET'])
def render_movie_list():
    file = open('C:/flask_tutorial/register_list.csv','r')
    reader = csv.reader(file)
    movies = list(reader)
    return render_template("registered.html", titel = "List of Movies", movies=movies)
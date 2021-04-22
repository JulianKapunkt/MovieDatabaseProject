
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, MovieModel, select_data
import csv
import sqlalchemy



users = {'mahdi': '123',
         'julian': '456',
         'richard': '789'}



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Sani43226117@localhost:5432/movie_rating"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
Migrate = Migrate(app, db)

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
            return render_template('register_movies.html', title = "Register new Movie")
        else:
            return render_template('login_failed.html', title= "Login Failed!")
    else:
        return render_template('login_failed.html', title= "Login Failed!")

@app.route("/register", methods = ['GET','POST'])

def register():
    if request.method == "POST":
        movie_name = request.form.get('moviename','None')
        year = request.form.get('year','None')
        try:
            # file = open('register_list.csv','a')  # a means append / r means read and w means write
            # writer = csv.writer(file)
            # writer.writerow((movie_name, year))
            # file.close()
            print(select_data())
            new_movie = MovieModel(name= movie_name, year= year)
            db.session.add(new_movie)
            db.session.commit()

        except Exception  as e:
            return e
        return render_template("registered_success.html", title= "Register Successfull")
    elif request.method == "GET":
        return render_template("register_movies.html", titel = "Register new Movie")



@app.route("/registered_movies", methods = ['GET'])
def render_movie_list():
    # with open('C:/flask_tutorial/register_list.csv','r') as file:
    #     reader = csv.reader(file)
    #     movies = list(reader)
    #     result = [movie for movie in movies if movie]
    result = select_data()
    return render_template("registered.html", titel = "List of Movies", movies=result)


if __name__ == "__main__":
    app.run(debug=True)
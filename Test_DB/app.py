
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import select_data
import csv
import sqlalchemy





app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Sani43226117@localhost:5432/movie_rating"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

#db.init_app(app)
#Migrate = Migrate(app, db)

@app.route("/")



def index():
    #name = request.args.get('var', 'World')
    #return render_template('index.html', name = name)
    result = select_data()
    b_result = str("user: "+result[0][0])
    return str(result[1])




if __name__ == "__main__":
    app.run(debug=True)
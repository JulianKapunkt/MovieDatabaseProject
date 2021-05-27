
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models_flask import select_data, db, databaseURI
import csv
import sqlalchemy





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = databaseURI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
#Migrate = Migrate(app, db)

@app.route("/")
def index():
    #name = request.args.get('var', 'World')
    #return render_template('index.html', name = name)
    result = select_data()
    print (len(result))
    b_result = str("username: "+ result[0].username + " pass: " + result[0].clear_password + " email: " + result[0].email)
    
    return  b_result




if __name__ == "__main__":
    app.run(debug=True)
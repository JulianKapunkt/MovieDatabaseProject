
from flask import Flask, request, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class RegistrationForm(FlaskForm):
    username  = StringField(label='username', validators=[Length(min=5,max=10,message="It is WRONG!")])


app = Flask(__name__)

app.config["SECRET_KEY"] = "VforVeronica"
Bootstrap(app)
@app.route("/")
def index():
    form = RegistrationForm(request.form)
    return render_template('signup.html', form=form)

@app.route("/signup", methods= ['POST'])
def signup():
    form = RegistrationForm(request.form)
    username = request.form.get('username','None')
    password = request.form.get('password','None')
    email    = request.form.get('email','None')
    if form.validate():
        return 'successful'
    else:
        return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
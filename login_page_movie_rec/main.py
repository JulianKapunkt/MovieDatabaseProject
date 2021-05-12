from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.config['SECRET_KEY'] = "Very Secret Key"
Bootstrap(app)


# class Login_Form(FlaskForm):
#     # Login Form Setup
#     email = StringField(label='E-Mail', validators=[DataRequired(),Email()])
#     password = PasswordField(label='Password', validators=[DataRequired(),Length(min=8)])
#     submit = SubmitField(label="Log In")

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login')
def login():
    # form = Login_Form()
    return render_template("login.html")

@app.route('/sign_up')
def sign_up():
    # form = Login_Form()
    return render_template("sign_up.html")

@app.route('/forgot_password')
def forgot_password():
    # form = Login_Form()
    return render_template("forgot_password.html")


if __name__ == "__main__":
    app.run(debug=True)
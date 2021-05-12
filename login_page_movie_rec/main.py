from flask import Flask, render_template, request
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


@app.route('/login' , methods =['GET', 'POST'])
def login():
    # form = Login_Form()
    if request.method == "POST":
        email = request.form.get("exampleInputEmail1")
        password = request.form.get("exampleInputPassword1")
        check = request.form.get("exampleCheck1")  # if checked, then the value is 'on' else 'null'
        return {'email': email , 'pass' : password, 'check': check}
    #return render_template("login.html")

@app.route('/sign_up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('exampleInputEmail1')
        password = request.form.get('exampleInputPassword1')
        password_repeated = request.form.get('exampleInputPassword2')
        if password == password_repeated:
            return {'username': username , 'email': email, 'pass': password}
        else:
            return "Password does not match"
    # form = Login_Form()
    elif request.method == 'GET':
        return render_template("sign_up.html")

@app.route('/forgot_password')
def forgot_password():
    # form = Login_Form()
    return render_template("forgot_password.html")

@app.route('/recover_user', methods = ['GET','POST'])
def recover_user():
    if request.method == 'POST':
        email = request.form.get('email')
        return email
if __name__ == "__main__":
    app.run(debug=True)
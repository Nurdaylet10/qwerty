from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Register')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    login = StringField("Login")

    password = PasswordField("Password")

    submit = SubmitField("Login")

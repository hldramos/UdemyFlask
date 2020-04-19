from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class FormLogin(FlaskForm):
    login = StringField("Login", validators=[
        Length(5, 20, "Login deve ter entre 5 e 20 caracteres.")])

    password = PasswordField("Password", validators=[
        Length(5, 20)])

    submit = SubmitField("Login")

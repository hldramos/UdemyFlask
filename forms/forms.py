from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class FormLogin(FlaskForm):
    login = StringField("Login", validators=[
        Length(5, 20, "Login deve ter entre 5 e 20 caracteres.")])

    password = PasswordField("Password", validators=[
        Length(5, 20)])

    submit = SubmitField("Login")


class FormUser(FlaskForm):
    name = StringField("Name", validators=[Length(
        5, 100, "Nome deve ter o minimo de 5 caracteres.")])

    login = StringField("Login", validators=[Length(
        5, 20, "Login deve ter o minimo de 5 caracteres.")])

    email = StringField("E-mail", validators=[Email()])

    password = PasswordField("Password", validators=[Length(
        5, 20, "Senha deve ter o minimo de 5 caracteres.")])

    submit = SubmitField("Cadastrar")

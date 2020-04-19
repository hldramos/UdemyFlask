from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class FormUser(FlaskForm):
    name = StringField("Name", validators=[Length(
        5, 100, "Nome deve ter o minimo de 5 caracteres.")])

    login = StringField("Login", validators=[Length(
        5, 20, "Login deve ter o minimo de 5 caracteres.")])

    email = StringField("E-mail", validators=[Email()])

    password = PasswordField("Password", validators=[Length(
        5, 20, "Senha deve ter o minimo de 5 caracteres.")])

    submit = SubmitField("Cadastrar")

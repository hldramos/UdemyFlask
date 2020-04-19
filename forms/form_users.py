from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class FormUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired])

    login = StringField("Login", validators=[DataRequired])

    email = StringField("E-mail", validators=[DataRequired])

    password = PasswordField("Password", validators=[DataRequired])

    submit = SubmitField("Cadastrar")

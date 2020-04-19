from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class Form_user(FlaskForm):
    name = StringField("Name", validators=[DataRequired],
                       render_kw={"placeholder": "Nome Completo "})

    login = StringField("Login", validators=[DataRequired],
                        render_kw={"placeholder": "Login "})

    email = StringField("E-mail", validators=[DataRequired],
                        render_kw={"placeholder": "E-mail "})

    password = PasswordField("Password", validators=[DataRequired],
                             render_kw={"placeholder": "Password "})

    submit = SubmitField("Cadastrar")

    logon = SubmitField("Login")

from flask import Flask

from ext import rotas, webui, database, configuracao, comandos, admin, login

from models.models import User, Product

from forms import forms


def create_app():
    app = Flask(__name__)
    configuracao.init_app(app)
    webui.init_app(app)
    database.init_app(app)
    comandos.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    rotas.init_app(app)

    return app

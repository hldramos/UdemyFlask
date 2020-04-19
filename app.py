from flask import Flask

from ext import rotas, webui, database, configuracao, comandos, admin, login

from models.users import User
from models.products import Product

from forms import form_users


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

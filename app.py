from flask import Flask

from ext import rotas, webui, database, configuracao, comandos
from models.users import User
from models.products import Product


def create_app():
    app = Flask(__name__)
    configuracao.init_app(app)
    webui.init_app(app)
    database.init_app(app)
    comandos.init_app(app)
    rotas.init_app(app)

    return app

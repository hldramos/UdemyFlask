from flask import request, redirect, url_for, render_template

from models.users import User
from models.products import Product


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/users")
    def users():
        usuario = User.query.all()
        return render_template("user.html", users=usuario)

    @app.route("/products")
    def products():
        produto = Product.query.all()
        return render_template("product.html", products=produto)

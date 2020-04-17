from flask import request, redirect, url_for, render_template

from ext.database import db

from models.users import User
from models.products import Product


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/users/")
    def users():
        usuario = User.query.all()
        return render_template("user.html", users=usuario)

    @app.route("/users/view/<int:id>")
    def view_users(id):
        usuario = User.query.get(id)
        return render_template("view_user.html", users=usuario)

    @app.route("/users/add")
    def add_users():
        usuario = User.query.all()
        return render_template("add_user.html", users=usuario)

    @app.route("/users/delete/<int:id>")
    def delete_user(id=0):
        usuario = User.query.filter_by(id=id).first()
        db.session.delete(usuario)
        db.session.commit()
        return redirect("/")

    @app.route("/products/")
    def products():
        produto = Product.query.all()
        return render_template("product.html", products=produto)

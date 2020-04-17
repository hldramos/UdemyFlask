from flask import request, redirect, url_for, render_template, flash
from flask_login import login_required, login_user, logout_user, LoginManager, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from ext.database import db

from models.users import User
from models.products import Product


def init_app(app):

    @app.route("/")
    def index():
        flash("OK")
        return render_template("index.html")

    @app.route("/users/", methods=["GET", "POST"])
    @login_required
    def users():
        usuario = User.query.all()
        return render_template("user.html", users=usuario)

    @app.route("/users/view/<int:id>/")
    @login_required
    def view_users(id):
        usuario = User.query.get(id)
        return render_template("view_user.html", users=usuario)

    @app.route("/users/add/")
    @login_required
    def add_users():
        usuario = User.query.all()
        return render_template("add_user.html", users=usuario)

    @app.route("/users/delete/<int:id>/")
    @login_required
    def delete_user(id=0):
        usuario = User.query.filter_by(id=id).first()
        db.session.delete(usuario)
        db.session.commit()
        return redirect("/")

    @app.route("/products/")
    def products():
        produto = Product.query.all()
        return render_template("product.html", products=produto)

    @app.route("/register/", methods=["POST", "GET"])
    @login_required
    def register():
        if request.method == "POST":
            user = User()
            user.name = request.form["name"]
            user.login = request.form["login"]
            user.email = request.form["email"]
            user.password = generate_password_hash(request.form["password"])

            db.session.add(user)
            db.session.commit()

        return redirect("/users")

    @app.route("/login/", methods=["POST", "GET"])
    def login():
        return render_template("login.html")

    @app.route("/logout/")
    @login_required
    def logout():
        # user = User.query.get(user_id)
        logout_user()

        return redirect("/")

    @app.route("/auth/", methods=["POST", "GET"])
    def auth():
        if request.method == "POST":
            login = request.form["login"]
            password = request.form["password"]

            user = User.query.filter_by(login=login).first()

            if not user:
                # flash("Credenciais inválidas!", category="error")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, password):
                # flash("Credenciais inválidas!", category="error")
                return redirect(url_for("login"))

            login_user(user)

            return redirect(url_for("index"))

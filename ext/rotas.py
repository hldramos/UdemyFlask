from flask import request, redirect, url_for, render_template, flash
from flask_login import login_required, login_user, logout_user, LoginManager, login_manager
from flask_wtf import Form
from werkzeug.security import generate_password_hash, check_password_hash

from ext.database import db

from forms.forms import FormUser, FormLogin

from models.models import User, Product


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
        form = FormUser()

        return render_template("add_user.html", form=form)

    @app.route("/users/delete/<int:id>/")
    @login_required
    def delete_user(id=0):
        usuario = User.query.filter_by(id=id).first()

        db.session.delete(usuario)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route("/products/")
    def products():
        produto = Product.query.all()

        return render_template("product.html", products=produto)

    @app.route("/register/", methods=["POST"])
    @login_required
    def register():
        form = FormUser()

        if form.validate_on_submit():
            user = User()

            user.name = form.name.data
            user.login = form.login.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            return redirect("/users")

        return render_template("add_user.html", form=form)

    @app.route("/login/", methods=["POST", "GET"])
    def login():
        form = FormLogin()

        return render_template("login.html", form=form)

    @app.route("/logout/")
    @login_required
    def logout():
        logout_user()

        return redirect("/")

    @app.route("/auth/", methods=["POST", "GET"])
    def auth():
        form = FormLogin()

        if form.validate_on_submit():
            form = FormLogin()
            login = form.login.data
            password = form.password.data
            user = User.query.filter_by(login=login).first()

            if not user:
                flash("Credenciais inválidas!", "danger")

                return redirect(url_for("login"))

            if not check_password_hash(user.password, password):
                flash("Credenciais inválidas!", "danger")
                # flash(form.errors, "waring")
                return redirect(url_for("login"))

            login_user(user)

            return redirect(url_for("index"))

        return render_template("login.html", form=form)

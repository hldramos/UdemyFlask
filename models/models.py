from ext.database import db
from flask_login import UserMixin


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    descricao = db.Column(db.String(150), unique=True, nullable=False)
    peso = db.Column(db.Integer())


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    password = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name

    def is_authenticated():
        pass

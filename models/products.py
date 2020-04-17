from ext.database import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    descricao = db.Column(db.String(150), unique=True, nullable=False)
    peso = db.Column(db.Integer())

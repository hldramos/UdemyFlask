from ext.database import db


def init_app(app):
    with app.app_context():
        db.create_all()

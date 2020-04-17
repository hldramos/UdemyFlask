from flask_login import LoginManager

from models.users import User


# @login_manager.user_loader
# def current_user(user_id):
#     return User.query.get(user_id)


def init_app(app):
    login_manager = LoginManager(app)

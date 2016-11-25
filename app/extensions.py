from flask_assets import Environment
from flask_login import LoginManager

from app.models import User

assets_env = Environment()

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(username):
    return User.find_by_username(username)

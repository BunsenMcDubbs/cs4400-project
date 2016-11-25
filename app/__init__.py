from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from app import assets
from app.controllers.main import main
from app.controllers.admin import admin

from app.extensions import (
    assets_env,
    login_manager
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    login_manager.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')

    return app

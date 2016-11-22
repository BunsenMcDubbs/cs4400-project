from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from app import assets
from app.controllers.main import main
from app.controllers.api import api

from app.extensions import (
    assets_env
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app

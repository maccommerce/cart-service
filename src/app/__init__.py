__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config.app_config import env_config
from .web.router.blueprints import api_blueprint
from .web.resources.shopping_cart import SingleItem, AllItems



api = Api(api_blueprint)
db = MongoEngine()


def app_factory(config_name: str) -> Flask:
    
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])
    env_config[config_name].init_app(app)

    api.init_app(app)
    db.init_app(app)
    api.add_resource(AllItems, '/cart')
    api.add_resource(SingleItem, '/cart_item')

    app.register_blueprint(api_blueprint)

    return app
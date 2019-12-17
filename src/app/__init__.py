__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config.app_config import env_config


# TODO ADD API BLUPRINTS
api = Api()

db = MongoEngine()


def app_factory(config_name: str) -> Flask:
    
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])
    env_config[config_name].init_app()

    api.init_app(app)
    db.init_app(app)


    # TODO add resource to api

    # TODO register app blueprint

    return app
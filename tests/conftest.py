import os
import pytest

from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
from flask_mongoengine import MongoEngine


from src.app import app_factory


def test_db_cleanup(db_url):

    with MongoClient(db_url) as connection:
        connection.shopping_cart.command(
            'dropUser',
            os.environ['MONGO_INITDB_ROOT_USERNAME']
        )

        connection.drop_database('shopping_cart')


def init_test_sandbox():

    db_url = os.environ["DATABASE_URL"] or "mongodb://localhost:27017/"

    with MongoClient(db_url) as connection:
        connection.shopping_cart.command(
            "createUser",
            os.environ['MONGO_INITDB_ROOT_USERNAME'],
            pwd=os.environ['MONGO_INITDB_ROOT_PASSWORD'],
            roles=[{'role':'readWrite','db':'shopping_cart'}]
        )

    return db_url

sandbox_db = init_test_sandbox()

@pytest.fixture
def client():
    # sandbox_db = init_test_sandbox()
    test_app = app_factory(config_name='test')
    test_app.config['DATABASE_URL'] = sandbox_db

    # yield test_app
    return test_app
    # test_db_cleanup(db_url=sandbox_db)

import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


load_dotenv("flask.env")

db = SQLAlchemy()
db_migration = Migrate()
ma = Marshmallow()


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)

    app.config.from_object(config_type)
    initialize_extensions(app)
    register_blueprint(app)

    return app


def initialize_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    ma.init_app(app)

    import core.models  # noqa: F401


def register_blueprint(app):

    from core.inventory_api import inventory_category_api_blueprint

    app.register_blueprint(inventory_category_api_blueprint, url_prefix="/api")

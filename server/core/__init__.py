import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from apifairy import APIFairy

from core.routes import register_routes
from lab.dynamodb import create_user, create_user_table, find_user


load_dotenv("flask.env")

root_dir = os.path.dirname(os.path.dirname(__file__))
template_dir = os.path.join(root_dir, "templates")
static_dir = os.path.join(root_dir, "static")

db = SQLAlchemy()
db_migration = Migrate()
ma = Marshmallow()
api_fairy = APIFairy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(
        __name__, template_folder=template_dir, static_folder=static_dir, static_url_path="/static"
    )

    app.config.from_object(config_type)
    initialize_extensions(app)
    register_blueprint(app)
    register_routes(app, db, bcrypt)

    # create_user_table()
    # create_user()
    # find_user()

    return app


def initialize_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    ma.init_app(app)
    api_fairy.init_app(app)
    login_manager.init_app(app)

    import core.models  # noqa: F401


def register_blueprint(app):

    from core.inventory_api import inventory_category_api_blueprint
    from core.user_api import user_api_bp

    app.register_blueprint(inventory_category_api_blueprint, url_prefix="/api")
    app.register_blueprint(user_api_bp, url_prefix="/api")


@login_manager.user_loader
def load_user(user_id):
    from core.models import User

    return User.query.get(user_id)


@login_manager.unauthorized_handler
def handle_unauthorized():
    return redirect(url_for("index"))

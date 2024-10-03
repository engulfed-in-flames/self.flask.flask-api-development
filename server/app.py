import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


load_dotenv("flask.env")


db = SQLAlchemy()
db_migration = Migrate()
ma = Marshmallow()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(
        __name__,
        # static_folder="static",
        # static_url_path="/static",
    )

    app.config.from_object(config_type)
    initialize_extensions(app)
    register_blueprint(app)
    register_apis(app)

    return app


def initialize_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    ma.init_app(app)
    login_manager.init_app(app)


def register_blueprint(app):

    from blueprints.core import core_bp
    from blueprints.account import account_bp
    from blueprints.localstack import localstack_bp

    app.register_blueprint(core_bp, url_prefix="/")
    app.register_blueprint(account_bp, url_prefix="/account")
    app.register_blueprint(localstack_bp, url_prefix="/localstack")


def register_apis(app):
    from apis import api

    api.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from blueprints.account.models import Account

    return Account.query.get(user_id)


@login_manager.unauthorized_handler
def handle_unauthorized():
    return redirect(url_for("core_bp.index"))


app = create_app()

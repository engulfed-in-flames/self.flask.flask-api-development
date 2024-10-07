import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(".env.dev")


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_object=os.getenv("CONFIG_OBJECT")) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprint(app)
    register_apis(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprint(app: Flask):
    from .blueprints.account import bp as account_bp
    from .blueprints.localstack import bp as localstack_bp
    from .blueprints.main import bp as core_bp
    from .blueprints.pydantic import bp as pydantic_bp

    app.register_blueprint(core_bp, url_prefix="/")
    app.register_blueprint(account_bp, url_prefix="/account")
    app.register_blueprint(localstack_bp, url_prefix="/localstack")
    app.register_blueprint(pydantic_bp, url_prefix="/pydantic")


def register_apis(app: Flask):
    from .apis import api

    api.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from .blueprints.account.models import Account

    return Account.query.get(user_id)


@login_manager.unauthorized_handler
def handle_unauthorized():
    return redirect(url_for("main.index"))

import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


load_dotenv(".env.dev")


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_object=os.getenv("CONFIG_OBJECT")) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprint(app: Flask):

    from blueprints.core import bp as core_bp
    from blueprints.account import bp as account_bp
    from blueprints.pydantic import bp as pydantic_bp
    from blueprints.localstack import bp as localstack_bp

    app.register_blueprint(core_bp, url_prefix="/")
    app.register_blueprint(account_bp, url_prefix="/account")
    app.register_blueprint(localstack_bp, url_prefix="/localstack")
    app.register_blueprint(pydantic_bp, url_prefix="/pydantic")


def register_apis(app: Flask):
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
register_extensions(app)
register_blueprint(app)
register_apis(app)

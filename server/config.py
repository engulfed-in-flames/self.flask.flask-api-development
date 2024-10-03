import os
from dataclasses import dataclass
from secrets import token_hex

from sqlalchemy.engine.url import URL


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@dataclass(frozen=True)
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")

    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = token_hex(32)

    TESTING = False
    DEBUG = os.getenv("FLASK_DEBUG")


@dataclass(frozen=True)
class DevelopmentConfig(Config):
    url_object = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
    )

    SQLALCHEMY_DATABASE_URI = url_object

    WTF_CSRF_ENABLED = False

    TESTING = True
    DEBUG = True


@dataclass(frozen=True)
class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False

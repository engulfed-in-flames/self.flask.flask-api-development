import os
from dataclasses import dataclass

from sqlalchemy.engine.url import URL


@dataclass(frozen=True)
class Config:
    SECRET_KEY = os.urandom(16)
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = os.getenv("FLASK_DEBUG")
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.urandom(32)


@dataclass(frozen=True)
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername=os.getenv("DB_DRIVER", "default_value"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
    )
    WTF_CSRF_ENABLED = False


@dataclass(frozen=True)
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername=os.getenv("DB_DRIVER", "default_value"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
    )
    WTF_CSRF_ENABLED = False


@dataclass(frozen=True)
class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False

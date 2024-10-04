from flask_restx import Api

from .ns_account import api as ns_account
from .ns_pydantic_account import api as ns_pydantic_account


api = Api(
    title="Flask API Development: Test Flask-RESTX",
    version="2.0",
    doc="/api/docs",
)

api.add_namespace(ns_account, path="/api/account")
api.add_namespace(ns_pydantic_account, path="/api/pydantic-account")

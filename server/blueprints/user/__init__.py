from flask import Blueprint

user_api_bp = Blueprint(
    "user_api",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401

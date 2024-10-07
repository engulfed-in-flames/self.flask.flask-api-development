from flask import Blueprint

bp = Blueprint(
    "localstack",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401
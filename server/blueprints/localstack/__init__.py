from flask import Blueprint

localstack_bp = Blueprint(
    "localstack_bp",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401

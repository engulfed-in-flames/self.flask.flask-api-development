from flask import Blueprint

inventory_bp = Blueprint(
    "inventory_bp",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401

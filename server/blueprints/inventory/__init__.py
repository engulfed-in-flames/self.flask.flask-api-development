from flask import Blueprint

inventory_category_api_blueprint = Blueprint(
    "inventory_category_api",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401

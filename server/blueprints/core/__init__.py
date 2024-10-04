from flask import Blueprint

bp = Blueprint(
    "core_bp",
    __name__,
    template_folder="templates",
)


from . import routes  # noqa: F401

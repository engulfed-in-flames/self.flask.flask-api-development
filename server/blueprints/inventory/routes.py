from apifairy import response
from core.models import Category
from . import inventory_category_api_blueprint
from .schema import CategorySchema

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route("/list", methods=["GET"])
@response(category_schema)
def category():
    return Category.query.all()

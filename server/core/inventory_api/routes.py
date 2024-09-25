from . import inventory_category_api_blueprint
from core.schema import CategorySchema
from core.models import Category
from apifairy import response

category_schema = CategorySchema(many=True)


@inventory_category_api_blueprint.route("/category", methods=["GET"])
@response(category_schema)
def category():
    return Category.query.all()

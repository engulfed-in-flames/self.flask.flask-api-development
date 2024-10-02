from apifairy import response
from . import inventory_bp
from .models import Category
from .schema import CategorySchema

category_schema = CategorySchema(many=True)


@inventory_bp.route("/list", methods=["GET"])
@response(category_schema)
def category():
    return Category.query.all()

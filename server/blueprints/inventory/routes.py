from . import inventory_bp
from .models import Category
from .schema import CategorySchema

category_schema = CategorySchema(many=True)

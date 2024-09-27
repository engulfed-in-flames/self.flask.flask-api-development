from core import ma
from marshmallow import fields


class CategorySchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)


class UserSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    is_admin = fields.Boolean(required=True)

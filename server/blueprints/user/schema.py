from core import ma
from marshmallow import fields


class UserSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    is_admin = fields.Boolean(required=True)

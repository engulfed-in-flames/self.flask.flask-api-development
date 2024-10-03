from marshmallow import fields
from app import ma


class AccountSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    is_admin = fields.Boolean(required=True)

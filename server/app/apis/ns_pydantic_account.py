from app.blueprints.pydantic.models import PydanticAccount
from flask_restx import Namespace, Resource, fields

api = Namespace("pydantic_accounts", description="APIs for Pydantic Accounts")


pydantic_account = api.model(
    "pydantic_account",
    {
        "uuid": fields.String(required=True, description="Your Pydantic Account UUID"),
        "email": fields.String(required=True, description="Your Pydantic Account Email"),
    },
)


@api.route("/")
class PydanticAccountListResource(Resource):
    @api.doc(name="retrieve_pydantic_accounts")
    @api.marshal_list_with(pydantic_account)
    def get(self):
        """Retrieves a list of accounts."""

        accounts = PydanticAccount.query.all()
        if not accounts:
            api.abort(404, message="No accounts found")
        return accounts


@api.route("/<int:id>")
class PydanticAccountResource(Resource):
    @api.doc(name="retrieve_a_pydantic_account", params={"id": "A record id"})
    @api.marshal_with(pydantic_account)
    def get(self, id: int):
        """Retrieves an account associated with the given id."""

        account = PydanticAccount.query.get(id)
        if not account:
            api.abort(404, message="Account not found")
        return account

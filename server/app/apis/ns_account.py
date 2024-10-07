from flask_restx import Namespace, Resource, fields

api = Namespace("account", description="APIs for Accounts")

account = api.model(
    "account",
    {
        "uuid": fields.String(required=True, description="Your Account UUID"),
        "email": fields.String(required=True, description="Your Account Email"),
        "created_at": fields.DateTime(
            required=True,
            description="DateTime When Your Account Was Created",
        ),
    },
)


ACCOUNTS: list[dict[str, str]] = [
    {"email": "account1@test.com", "name": "Abraham"},
    {"email": "account2@test.com", "name": "Bob"},
    {"email": "account3@test.com", "name": "Cerberus"},
    {"email": "account4@test.com", "name": "Francis"},
]


@api.route("/")
class AccountList(Resource):
    @api.doc("list_accounts")
    @api.marshal_list_with(account)
    def get(self):
        """Shows a list of all accounts"""
        return ACCOUNTS

    def post(self): ...


@api.route("/<int:index>")
class Account(Resource):
    @api.doc(name="get_account", params={"index": "An index for the account list"})
    @api.marshal_with(account)
    def get(self, index: int):
        """Shows an account given the index"""
        if index >= len(ACCOUNTS):
            api.abort(404)
        return ACCOUNTS[index]

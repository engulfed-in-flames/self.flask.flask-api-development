from . import user_api_bp

from core.schema import UserSchema
from core.models import User
from apifairy import response

user_schema = UserSchema(many=True)


@user_api_bp.route("/user", methods=["GET"])
@response(user_schema)
def users():
    return User.query.all()


# @user_api_bp.route("/user", methods=["GET"])
# @response(user_schema)
# def user(): ...

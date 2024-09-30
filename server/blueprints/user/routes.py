from flask import render_template
from apifairy import response
from core.models import User
from . import user_api_bp
from .schema import UserSchema

user_schema = UserSchema(many=True)


@user_api_bp.route("/list", methods=["GET"])
@response(user_schema)
def users():
    return User.query.all()


@user_api_bp.route("/list-on-html", methods=["GET"])
def users_on_html():
    users = User.query.all()
    return render_template("user/index.html", users=users)


# @user_api_bp.route("/user", methods=["GET"])
# @response(user_schema)
# def user(): ...

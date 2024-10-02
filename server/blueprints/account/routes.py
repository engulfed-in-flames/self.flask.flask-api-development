from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from apifairy import response

from app import db, bcrypt
from . import account_bp
from .models import User
from .schema import UserSchema
from .forms import SignupForm, LoginForm

user_schema = UserSchema(many=True)


@account_bp.route("/list", methods=["GET"])
@response(user_schema)
def users():
    return User.query.all()


@account_bp.route("/list-on-html", methods=["GET"])
def users_on_html():
    users = User.query.all()
    return render_template("account/index.html", users=users)


@account_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("core_bp.index"))

    form = SignupForm(request.form)
    if request.method == "GET":
        return render_template("account/signup.html", form=form)

    if request.method == "POST" and form.validate():
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)

        return redirect(url_for("core_bp.index"))


@account_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("core_bp.index"))

    form = LoginForm(request.form)
    if request.method == "GET":
        return render_template("account/login.html", form=form)

    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("core_bp.index"))
        else:
            form.password.errors.append("Email or password is invalid.")
            return render_template("account/login.html", form=form)


@account_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core_bp.index"))

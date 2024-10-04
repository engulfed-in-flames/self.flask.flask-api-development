from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app import db, bcrypt
from . import bp
from .models import Account
from .forms import SignupForm, LoginForm


@bp.route("/list-on-html", methods=["GET"])
def accounts_on_html():
    accounts = Account.query.all()
    return render_template("account/index.html", accounts=accounts)


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("core_bp.index"))

    form = SignupForm(request.form)

    if request.method == "POST" and form.validate():
        try:
            email = form.email.data
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

            account = Account(email=email, password=hashed_password)
            db.session.add(account)
            db.session.commit()
            login_user(account)
            return redirect(url_for("core_bp.index"))
        except:
            db.session.rollback()

    return render_template("account/signup.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("core_bp.index"))

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        account = Account.query.filter_by(email=form.email.data).first()

        if account and bcrypt.check_password_hash(account.password, form.password.data):
            login_user(account)
            return redirect(url_for("core_bp.index"))
        else:
            form.password.errors.append("Email or password is invalid.")

    return render_template("account/login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core_bp.index"))

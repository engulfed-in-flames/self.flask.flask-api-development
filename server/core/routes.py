from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            if current_user.is_authenticated:
                return redirect(url_for("index"))
            return render_template("signup.html")
        if request.method == "POST":
            from core.models import User

            email = request.form.get("email")
            password = request.form.get("password")

            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            user = User(email=email, password=hashed_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            if current_user.is_authenticated:
                return redirect(url_for("index"))
            return render_template("login.html")
        elif request.method == "POST":
            from core.models import User

            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return render_template("index.html")
            else:
                return "Login Failed"

    @app.route("/logout")
    def logout():
        logout_user()
        return render_template("index.html")

    @app.route("/secret")
    @login_required
    def secret():
        return "This is a private page!"

import os
from flask import request, make_response, render_template, redirect, url_for, send_file, session
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

    @app.route("/<int:n1>/<int:n2>")
    def handle_url_params(n1, n2):
        return f"{n1} + {n2} = {n1 + n2}"

    @app.route("/query")
    def handle_url_query_params():
        if len(request.args) == 0:
            return "There is no query params at all."

        queries = ""
        for key, value in request.args.items():
            queries += f"{key}: {value}<br/>"

        return queries

    @app.route("/response")
    def handle_response():
        response = make_response("Hello, World!")
        response.status_code = 202
        response.headers["content-type"] = "text/plain"

        return response

    @app.route("/file", methods=["GET", "POST"])
    def handle_file():
        if request.method == "GET":
            return render_template("upload_file.html")
        elif request.method == "POST":
            file = request.files["file"]  # The name of input

            if file.content_type in ["image/jpeg", "image/png", "image/gif", "image/webp"]:
                storage_dir = os.path.join(
                    os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "storage"
                )
                os.makedirs(storage_dir, exist_ok=True)

                file_path = os.path.join(storage_dir, str(file.filename))
                file.save(file_path)

                return send_file(file_path, as_attachment=False)
            else:
                return "Invalid file type. Please, upload an image."

    @app.route("/set-session")
    def set_session():
        session["foo"] = "bar"

        return "<h1>Set Session Data</h1>"

    @app.route("/get-session")
    def get_session():
        if len(session) == 0:
            return "<h1>No Session Found</h1>"

        value1 = session.get("foo", "Undefined")
        value2 = session.get("bar", "Undefined")

        return render_template("get_session.html", values=[value1, value2])

    @app.route("/clear-session")
    def clear_session():
        session.clear()

        return "<h1>Session Clear</h1>"

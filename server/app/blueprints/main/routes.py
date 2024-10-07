from flask import make_response, render_template, request
from flask_login import login_required

from . import bp


@bp.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")


@bp.route("/secret")
@login_required
def secret():
    return "<h1>This is a private page!</h1>"


@bp.route("/<int:n1>/<int:n2>")
def handle_url_params(n1, n2):
    return f"{n1} + {n2} = {n1 + n2}"


@bp.route("/query")
def handle_url_query_params():
    if len(request.args) == 0:
        return "<h1>There is no query params at all.</h1>"

    queries = []
    for key, value in request.args.items():
        queries.append(f"{key}: {value}<br/>")

    return "".join(queries)


@bp.route("/response")
def handle_response():
    response = make_response("Hello, World!")
    response.status_code = 202
    response.headers["content-type"] = "text/plain"

    return response


# import os

# from flask import send_file, session

# @bp.route("/file", methods=["GET", "POST"])
# def handle_file():
#     if request.method == "GET":
#         return render_template("upload_file.html")

#     if request.method == "POST":
#         file = request.files["file"]  # The name of input

#         if file.content_type in ["image/jpeg", "image/png", "image/gif", "image/webp"]:
#             storage_dir = os.path.join(
#                 os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "storage"
#             )
#             os.makedirs(storage_dir, exist_ok=True)

#             file_path = os.path.join(storage_dir, str(file.filename))
#             file.save(file_path)

#             return send_file(file_path, as_attachment=False)
#         else:
#             return "Invalid file type. Please, upload an image."


# @bp.route("/set-session")
# def set_session():
#     session["foo"] = "bar"

#     return "<h1>Session Data Set</h1>"


# @bp.route("/get-session")
# def get_session():
#     if len(session) == 0:
#         return "<h1>No Session Found</h1>"

#     value1 = session.get("foo", "Undefined")
#     value2 = session.get("bar", "Undefined")

#     return render_template("main/get_session.html", values=[value1, value2])


# @bp.route("/clear-session")
# def clear_session():
#     session.clear()

#     return "<h1>Session Clear</h1>"

from flask import jsonify, redirect, request, url_for
from flask.ext.login import login_required, login_user

from website.accounts import authenticate
from website.server.authentication import User


def login():
    """
    Process a form-data based login. Redirect to the front page on success,
    error otherwise.
    """
    validation_msg = "Login request must contain form encoded username and " \
                     "password fields, with string values."
    if not request.form:
        return jsonify({"error": validation_msg}), 401

    validated = all(
        [
            isinstance(request.form.get("username"), basestring),
            isinstance(request.form.get("password"), basestring)
        ]
    )
    if not validated:
        return jsonify({"error": validation_msg}), 401

    user = User(request.form.get("username"))

    if authenticate(user.id, request.form.get("password")):
        login_user(user)
        return redirect(url_for("index", _external=True, _scheme="https"))
    else:
        return jsonfiy({"error": "Authentication failed"}), 401

import website

from flask import Flask, jsonify, render_template, request
from werkzeug import exceptions


def build_application():
    app = Flask(__name__)
    return app


app = build_application()


@app.route('/')
def index():
    """
    Returns the frontpage.
    """
    return render_template('index.html')


# Version endpoint
@app.route('/version')
def version():
    """
    Returns version JSON.
    """
    info = {
        "ok": True,
        "version": website.__version__,
    }

    return jsonify(info)


@app.route('/account', methods=["POST"])
def new_user():
    """
    Create a new user. Expects the following JSON data:
      - username: the desired username
      - password: the desired password
    """
    if not request.json:
        raise exceptions.BadRequest("Request must include JSON content")

    username = request.json.get("username")
    password = request.json.get("password")

    if None in [username, password]:
        raise exceptions.BadRequest(
            "Request must include JSON username and password."
        )

    ack = accounts.create_account(username, password)
    return jsonify({"created": ack.inserted_id}), 201

if __name__ == "__main__":
    app.run()




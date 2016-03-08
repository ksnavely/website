import website
from website import accounts

from flask import Flask, jsonify, render_template, request


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
        return jsonify({"error": "Request must include JSON content"}), 400

    username = request.json.get("username")
    password = request.json.get("password")

    if None in [username, password]:
        return jsonify({"error": "Request must include JSON username and password."}), 400

    ack = accounts.create_account(username, password)
    return jsonify({"created": ack.inserted_id}), 201

if __name__ == "__main__":
    app.run()

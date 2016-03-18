import website
from website.server.views import account, frontpage, version

from flask import Flask, jsonify, render_template, request


def build_application():
    app = Flask(__name__)
    return app


app = build_application()

app.add_url_rule("/", "index", frontpage.index, methods=["GET"])
app.add_url_rule("/account", "account", account.new_user, methods=["POST"])
app.add_url_rule("/version", "version", version.version, methods=["GET"])


if __name__ == "__main__":
    app.run()

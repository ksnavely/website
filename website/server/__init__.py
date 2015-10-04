import website

from flask import Flask, jsonify

def build_application():
    app = Flask(__name__)
    return app

app = build_application()

# Version endpoint
@app.route('/')
def version():
    """
    Returns version JSON.
    """
    info = {
        "ok": True,
        "version": website.__version__,
    }

    return jsonify(info)

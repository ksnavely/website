import website

from flask import Flask, jsonify, render_template

def build_application():
    app = Flask(__name__)
    return app

app = build_application()

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

@app.route('/')
def index():
    """
    Returns frontpage
    """
    return render_template('index.html')

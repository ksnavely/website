from flask import render_template


def index():
    """
    Returns the frontpage.
    """
    return render_template('index.html')

import arrow
from flask import render_template

from website import blog


def index():
    """
    Returns the frontpage.
    """
    return render_template('index.html', blog_posts=blog.get_posts())

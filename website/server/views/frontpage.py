import arrow
from flask import render_template, request

from website import blog


def index():
    """
    Returns the frontpage.
    """
    date = request.args.get("date")
    return render_template(
        'index.html',
        blog_posts=blog.get_posts(date=date)
    )

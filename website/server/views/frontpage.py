import arrow
from flask import redirect, render_template, request, url_for
from flask.ext.login import login_required

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


def create_blog_entry():
    """
    View the new blog post page.
    """
    return render_template(
        'create_post.html',
    )


@login_required
def create_blog_entry_submit():
    """
    Creates a new blog post.
    """
    if not request.form:
        return (
            "create_blog_entry: Blog entry form data is required.",
            404)


    required_fields = ["title", "tags", "text", "author"]

    if not all([r in request.form.keys() for r in required_fields]):
        return ("create_blog_entry: Blog entries require the following"
                " fields: {0}".format(required_fields)), 404

    p = request.form
    tags = [t.strip() for t in p["tags"].split(",")]
    post_info = blog.create_post(
        p["title"],
        p["author"],
        p["text"],
        tags=tags
    )

    return redirect(url_for("index", _external=True, _scheme="https"))

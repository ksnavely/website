"""
_blog_

Create/read blog posts from a database.
"""
import arrow
from pymongo import MongoClient as MC

# Public interface

def create_post(title, author, text, tags=None):
    tags = tags or []
    post = {
        "title": title,
        "author": author,
        "text": text,
        "date": arrow.utcnow(),
        "tags": tags
    }
    return _get_blog_posts_collection().insert_one(post)


def get_posts(date=None):
    """
    :param str date: A date substring for a regex used in the mongo
        find like "2016-3"
    """
    if date:
		cursor = _get_blog_posts_collection().find({"date": {"$regex": date}})
    else:
		cursor = _get_blog_posts_collection().find()

    blogs = list(cursor)
    return blogs


# Private interface


def _client():
    global CLIENT
    if CLIENT is None:
        CLIENT = MC()
    return CLIENT


def _get_blog_posts_collection():
    return _client().blog.posts

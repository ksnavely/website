"""
_blog_

Create/read blog posts from a database.
"""
import arrow
from bson.objectid import ObjectId
from pymongo import MongoClient as MC


CLIENT = None


# Public interface


def create_post(title, author, text, tags=None):
    tags = tags or []
    post = {
        "title": title,
        "author": author,
        "text": text,
        "date": arrow.utcnow().for_json(),
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

    blogs = sorted(list(cursor), key=lambda x: x["date"], reverse=True)
    return blogs


def get_post(post_id):
    """"
    Get a single post.

    :param str post_id: The mongo id for the blog post.

    :returns: A dict of post attributes, or None if post_id is not
        found in mongo.
    """
    post = _get_blog_posts_collection().find_one(
        {"_id": ObjectId(post_id)}
    ) 
    return post


def update_post(post_id, title, author, text, date, tags):
    tags = tags or []
    selector = {"_id": ObjectId(post_id)}
    post = {
        "title": title,
        "author": author,
        "text": text,
        "date": date,
        "tags": tags
    }
    return _get_blog_posts_collection().update_one(selector, {"$set": post})


# Private interface


def _client():
    global CLIENT
    if CLIENT is None:
        CLIENT = MC()
    return CLIENT


def _get_blog_posts_collection():
    return _client().blog.posts

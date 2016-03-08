# Major WIP
import hashlib
import base64
import uuid

import arrow
import bcrypt
from pymongo import MongoClient as MC

CLIENT = None


# Module interface

def create_account(username, password):
    hashed_pw = _get_hashed_password(password)
    doc = {
              "_id": username,
              "username": username,
              "hashed_password": hashed_pw,
              "signup_date": arrow.utcnow().timestamp
    }
    return _get_auth_collection().insert_one(doc)


def authenticate(username, password):
    doc = _get_auth_collection().find_one({"_id": username})
    return _check_password(password, doc["hashed_password"])


# Private interface


def _client():
    global CLIENT
    if CLIENT is None:
        CLIENT = MC()
    return CLIENT


def _get_auth_collection():
    return _client().accounts.auth


def _get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def _check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

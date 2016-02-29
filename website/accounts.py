# Major WIP
import hashlib
import base64
import uuid

import bcrypt
from pymongo import MongoClient as MC

CLIENT = None


def _client():
    if CLIENT is None:
        CLIENT = MC()
    return CLIENT


def _get_auth_collection():
    return _client().accounts.auth


def _create_account(username, password):
    hashed_pw = _get_hashed_password(password)
    doc = {
              "_id": username,
              "username": username,
              "hashed_password": hashed_pw
    } 
    _get_auth_collection().insert_one(doc)


def _get_hashed_password(password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def _check_password(password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password) 

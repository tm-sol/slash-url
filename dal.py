from pymongo import MongoClient
from bson.objectid import ObjectId
import utils

"""Data access layer used to connect to DB"""

client = MongoClient('localhost', 27017)
#  Connect to production Database
db = client.ProdDB


def add_url(url):
    #  Inserts a valid url and returns a hashed database ID
    result = db['urls'].insert_one({"url": url})
    return utils.encode(str(result.inserted_id))


def lookup_url(code):
    #  Takes a potentially hashed value and attempts to decode before finding a match.  Returns paired url if found.
    result = db['urls'].find_one({"_id": ObjectId(utils.decode(code))})
    if result["url"] is None:
        return None
    return result["url"]

from pymongo import MongoClient
from bson.objectid import ObjectId
import utils

client = MongoClient('localhost', 27017)
db = client.TestDB


def add_url(url):
    result = db['urls'].insert_one({"url": url})
    return utils.encode(str(result.inserted_id))


def lookup_url(code):
    result = db['urls'].find_one({"_id": ObjectId(utils.decode(code))})
    if result["url"] is None:
        return None
    return result["url"]

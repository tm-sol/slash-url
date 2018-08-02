from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.TestDB


def add_url(url):
    result = db['urls'].insert_one({"url": url})
    return str(result.inserted_id)


def lookup_url(code):
    result = db['urls'].find_one({"_id": ObjectId(code)})
    if result["url"] is None:
        return None
    return result["url"]

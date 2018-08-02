import unittest
from pymongo import MongoClient
import dal


class TestDB(unittest.TestCase):

    def setUp(self):
        # Connect to test Database & drop collection faster than dropping whole DB
        self.dal = dal
        db = MongoClient('localhost', 27017).TestDB
        db.drop_collection('urls')

        self._id = db['urls'].insert_one({"url": 'https://www.python.org/'})
        self.dal.db = db

    def tearDown(self):
        self.dal.db.drop_collection('urls')

    def test_add_url(self):
        self.assertEqual(len(self.dal.add_url("www.google.com")), 20)

    def lookup_url(self):
        self.assertEqual(len(self.dal.lookup_url(self._id)), 'https://www.python.org/')

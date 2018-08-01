import unittest
from app import app as webapp
import json


class TestApp(unittest.TestCase):

    def test_valid_url(self):
        self.webapp = webapp.test_client()
        response = self.webapp.get('/shorten_url')
        self.assertEqual(response._status_code, 400)


import unittest
from app import app as webapp
import json


class TestApp(unittest.TestCase):

    def test_invalid_url(self):
        self.app = webapp.test_client()
        response = self.app.post('/shorten_url',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(dict(url='ww.w.google.com')))
        self.assertEqual(response._status_code, 400, "check bad request format code returned")

    def test_valid_url(self):
        self.app = webapp.test_client()
        response = self.app.post('/shorten_url',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(dict(url='www.google.com')))
        self.assertEqual(response._status_code, 201, "check created error code returned")

    def test_redirect(self):
        self.app = webapp.test_client()
        response = self.app.get('/shorten_url/www.google.com')
        self.assertEqual(response._status_code, 302, "check identified as valid url and forwarded")

import unittest
import utils


class TestUtils(unittest.TestCase):

    PREFIX_REGEX = "^(http|https|ftp)://.+"

    def setUp(self):
        self.valid_urls = ["http://www.google.com", "http://google.com", "http://www.google.com", "https://www.google.com"]
        self.invalid_urls = ["http://w.ww.google.com", "http://www.google", "mailto:test@google.com]", "google.com"]
        self.url_missing_prefix = ["google.com", "google", "www.google.com"]

    def test_convert_url(self):
        for url in self.url_missing_prefix:
            self.assertRegex(utils.convert(url), self.PREFIX_REGEX, "check a valid prefix is added")

    def test_check_url(self):
        for url in self.valid_urls:
            self.assertTrue(utils.check_url(url), "check valid urls as understood pass")

        for url in self.invalid_urls:
                self.assertFalse(utils.check_url(url), "check invalid urls fail")


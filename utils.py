import requests.exceptions
from hashids import Hashids

"""A collection of tooling used throughout application."""


def encode(_id):
    #  Encodes _id from MongoDB to shorten and obfuscate
    return Hashids().encode_hex(_id)


def decode(code):
    #  Decodes code into a searchable _id for MongoDB
    return Hashids().decode_hex(code)


def convert(url):
    #  Add missing prefix if required.  Refactor to extend for different formats
    if not (url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://')):
        return 'http://{}'.format(url)
    return url


def check_url(url):
    #  Checks a valid url by checking if the url is accessible as a request
    try:
        requests.get(url)
        return True
    except IOError:
        return False


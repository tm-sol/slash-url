import requests.exceptions
from requests.exceptions import ConnectionError, InvalidSchema, MissingSchema


def convert(url):
    if not (url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://')):
        return 'http://' + url
    return url


def check_url(url):
    try:
        requests.get(url)
        return True
    except ConnectionError:
        return False
    except InvalidSchema:
        return False
    except MissingSchema:
        return False
    except IOError:
        return False

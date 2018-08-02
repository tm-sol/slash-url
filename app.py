from flask import Flask, request
from flask_api import status
import utils


app = Flask(__name__)


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    if request.is_json:
        url = request.get_json()["url"]
        if utils.check_url(utils.convert(url)):
            return '', status.HTTP_201_CREATED
    return 'Malformed URL: {}'.format(url), status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)

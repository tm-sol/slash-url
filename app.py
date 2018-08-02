from flask import Flask, request, redirect, jsonify
from flask_api import status
import utils
import data

HOST = 'http://127.0.0.1:5000/'
app = Flask(__name__)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    if request.is_json:
        url = request.get_json()["url"]
        if utils.check_url(utils.convert(url)):
            return HOST+data.add_url(url), status.HTTP_201_CREATED
    return 'Malformed URL: {}'.format(url), status.HTTP_400_BAD_REQUEST


@app.route('/<code>', methods=['GET'])
def redirect_url(code):
    if utils.check_url(utils.convert(code)):
        return redirect(utils.convert(code), code=302)
    else:
        try:
            result = data.lookup_url(code)
            if result:
                return redirect(utils.convert(result), code=302)
            else:
                return 'Malformed URL: {}{}'.format(HOST, code), status.HTTP_400_BAD_REQUEST
        except Exception:
            return 'Malformed URL: {}{}'.format(HOST, code), status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
from flask_api import status

app = Flask(__name__)


@app.route('/shorten_url', methods=['GET'])
def get_shortened_url():
    return 'Malformed URL', status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)

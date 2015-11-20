from flask import Flask, request
from flask.json import jsonify

from solver import compute

app = Flask(__name__)


@app.route("/max_queens", methods=['post'])
def max_queens():
    request_input = request.get_json()
    queens_list = compute(**request_input)
    return jsonify(
        added_queens=[dict(x=x, y=y) for x, y in queens_list]
    )


if __name__ == "__main__":
    app.run('localhost', 8080)

import os

from flask import Flask, jsonify, request, abort
from utils import answer_from_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    query = request.json
    cmd1 = query.get("cmd1")
    cmd2 = query.get("cmd2")
    value1 = query.get("value1")
    value2 = query.get("value2")
    filename = query.get("filename")

    if not (cmd1 and value1 and filename):
        abort(400)

    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        abort(400)

    with open(file_path) as file:
        res = answer_from_query(cmd1, value1, file)
        if cmd2 and value2:
            res = answer_from_query(cmd2, value2, res)
        return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)

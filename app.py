from flask import Flask, jsonify
from flask import request
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    first_name = request_data["first_name"].capitalize()
    last_name = request_data["last_name"].capitalize()
    email = request_data["email"]
    domain = email[email.index('@') + 1 : ]
    return jsonify({"first_name": first_name, "last_name": last_name, "email": email, "domain" : domain})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

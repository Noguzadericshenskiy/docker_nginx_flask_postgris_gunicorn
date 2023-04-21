import os
from flask import Flask, send_from_directory
from sqlalchemy.dialects.postgresql import insert


app = Flask(__name__)


# @app.route("/coffee")
# def get_all_coffee():
#     ...
#
#
# @app.route("/add_user", methods=["POST"])
# def get_all_users():
#     ...
#
# @app.route("/users", methods=["GET"])
# def get_all_users():
#     ...


@app.route("/")
def hello_world():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# docker compose up
# docker compose -f docker-compose.yml down -v
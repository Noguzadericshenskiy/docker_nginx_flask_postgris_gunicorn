import os
import json
from flask import Flask, send_from_directory, jsonify
from sqlalchemy.dialects.postgresql import insert

from db import session, Base, engine
from models import User, Coffee
from fill_db import fill_db


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fill_db()


@app.route("/add_user", methods=["POST"])
def add_user():
    """ Добавление пользователя.
    В ответе информация о новом пользователе с его предпочтением по кофе."""
    insert_query = insert(User).values(
        name="Vasyan",
        has_sale=True,
        coffee_id=5,
        address=json.dumps({"id": 9957, "uid": "07790388-e8ed-4456-9f9b-9897f8fbbfc8"})).\
        returning(User)
    # do_nothing_stmt = insert_query.on_conflict_do_nothing(index_elements=['name']).\
    #     returning(User.name, User.has_sale, User.coffee_id)
    user_add = session.execute(insert_query)
    session.commit()
    user_obj = session.query(User).where(User.id == user_add['id'])

    return 'user_add'


@app.route("/all_users", methods=['GET'])
def get_all_users():
    users_list = []
    users = session.query(User).all()
    for user in users:
        user_obj = user.to_json()
        user_obj['coffee'] = user.coffee.to_json()
        users_list.append(user_obj)

    return jsonify(users_list)


# @app.route("/users", methods=["GET"])
# def get_all_users():
#     ...


@app.route("/")
def hello_world():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

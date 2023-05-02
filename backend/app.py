import os
import json

from flask import Flask, send_from_directory, jsonify, request
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select
from typing import Dict, Any, Optional, List

import models

from db import session, Base, engine
from models import User, Coffee
from fill_db import fill_db
from schemas import schema


app = Flask(__name__)


def get_user_by_id(id):
    user = session.query(User).where(User.id == id).one()
    user_obj = user.to_json()
    user_obj['coffee'] = user.coffee.to_json()
    return user_obj


# @app.before_first_request
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
        address=json.dumps({"id": 7388, "uid": "09042327-f80b-4cc0-ba16-9b57b0217868",
                               "city": "Margaretatown", "street_name": "Lizeth Coves",
                               "zip_code": "42687"}),
        coffee_id=5
    ).returning(User.id)
    user_stmt = session.execute(insert_query).one()
    session.commit()
    new_user = get_user_by_id(user_stmt[0])

    return json.dumps(new_user, indent=4), 201


@app.route("/all_users", methods=['GET'])
def get_all_users():
    users_list = []
    users = session.query(User).all()
    for user in users:
        user_obj = get_user_by_id(user.id)
        users_list.append(user_obj)

    return jsonify(users_list), 200


@app.route('/get_coffee/', methods=['GET'])
def search_coffee_by_title():
    """Поиск кофе по названию"""
    string_search = request.args.get("coffee_title")
    coffee_list = []
    coffee_query = select(Coffee).where(Coffee.title.match(string_search))
    coffee_stmt = session.execute(coffee_query).all()
    for coffee_obj in coffee_stmt:
        coffee = coffee_obj[0].to_json()
        coffee_list.append(coffee)
    return json.dumps(coffee_list, indent=4), 200


# , response_model=List[schema.UserOut]
@ app.route("/get_user_by_country", methods=['GET'])
def get_user_by_country():
    """Список пользователей, проживающих в стране"""
    users_list = []
    country = request.args.get("country")
    users = session.query(User).where(User.address["country"].as_string() == country).all()

    for user in users:
        user_obj = user.to_json()
        response_model = user.schema.UserOut()
        print(response_model)
        users_list.append(user_obj)

    return json.dumps(users_list, indent=4), 200


@app.route("/unique_alement", methods=['GET'])
def unique_element():
    """Список уникальных элементов в заметках к кофе."""
    list_unique_elements = []

    id = request.args.get("id")

    notes = session.query(Coffee.notes).filter(Coffee.id == id).scalar()

    for i in notes:
        result = session.query(Coffee).where(Coffee.notes.any(i)).count()
        if result == 1:
            list_unique_elements.append(i)
    return jsonify(list_unique_elements)


@app.route("/")
def hello_world():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import json
from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql.expression import cast
from flask import jsonify
from typing import Dict, Any, Optional

from loguru import logger

from models import Coffee, User
from fill_db import fill_db
from db import engine, Base, session


logger.debug("Simple logging.")


def before_first_request():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_all_users():
    users_list = []
    users = session.query(User).all()
    for user in users:
        user_obj = get_user_by_id(user.id)
        users_list.append(user_obj)

    print(json.dumps(users_list, indent=4))


def get_user_by_id(id):
    user = session.query(User).where(User.id == id).one()
    user_obj = user.to_json()
    user_obj['coffee'] = user.coffee.to_json()
    return user_obj


@logger.catch
def add_user():
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
    print(json.dumps(new_user, indent=4))


@logger.catch
def search_coffee_by_title(string_search):
    " -> Dict[str, Any]"
    # coffee = session.query(Coffee).where(Coffee.title=="")
    coffee_list = []
    coffee_query = select(Coffee).where(Coffee.title.match(string_search))
    coffe_stmt = session.execute(coffee_query).all()
    for coffee_obj in coffe_stmt:
        coffee = coffee_obj[0].to_json()
        coffee_list.append(coffee)
    print(coffee_list)


@logger.catch
def unic_element(string_search):
    "Список уникальных элементов в заметках к кофе."
    elements = []
    element_query = select(Coffee).where(Coffee.notes.match(string_search) == False)
    return 'ok'


# @logger.catch
def get_user_by_country(country):
    # user = session.query(User).where(json.loads(User.address)['country'] == country).one()
    # user = session.query(User).where(User.id == 1).one()

    # user = session.query(User).filter(User.address.comparator.contains(["country"])).all()
    # user = session.query(User.address).filter(User.address["id":"3097"].as_string() != '3097').all()
    user = session.query(User.address).first()
    # where(
    #     func.json_contains(Foo.bar, func.json_object("country", "some_value"))

    # user_obj = user.to_json()
    # user_obj['coffee'] = user.coffee.to_json()
    # print(json.dumps(user_obj, indent=4))
    print(user)


def foo():
    ...

if __name__ == "__main__":
    before_first_request()
    fill_db()

    # add_user()
    # add_user()
    # search_coffee_by_title("Green Coffee")
    # search_coffee_by_title("Green")
    # search_coffee_by_title("green")
    # get_user_by_country('Spain')
    get_all_users()
    # add_user()
    # read()
    # add_coffee()

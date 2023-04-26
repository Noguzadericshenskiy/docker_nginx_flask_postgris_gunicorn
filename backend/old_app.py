import json
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
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
    fill_db()


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

# def add_user():
#     user = User()
#     user.name = "Vasyan"
#     user.has_sale = True
#     user.address = json.dumps({"id": 7388, "uid": "09042327-f80b-4cc0-ba16-9b57b0217868",
#                                "city": "Margaretatown", "street_name": "Lizeth Coves",
#                                 "zip_code": "42687"})
#     user.coffee_id = 5
#     session.add(user)
#     session.commit()

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


if __name__ == "__main__":
    # fill_db()
    # add_user()
    # add_user()
    # search_coffee_by_title("Green Coffee")
    # search_coffee_by_title("Green")
    search_coffee_by_title("green")
    # get_all_users()
    # add_user()
    # read()
    # add_coffee()

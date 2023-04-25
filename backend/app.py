import os
from flask import Flask, send_from_directory, jsonify
from sqlalchemy.dialects.postgresql import insert

from db import session
from models import User, Coffee

app = Flask(__name__)


# @app.route("/coffee")
# def get_all_coffee():
#     ...


@app.route("/add_user", methods=["POST"])
def add_user():
    """ Добавление пользователя.
    В ответе информация о новом пользователе с его предпочтением по кофе."""
    insert_query = insert(User).values(
        # id=11,
        name="Vasyan",
        has_sale=True,
        coffee_id=5,
        # address='{"id": 9957, '
        # '"uid": "07790388-e8ed-4456-9f9b-9897f8fbbfc8", '
        # '"city": "Lake Evelin", '
        # '"street_name": "Christy Points", '
        # '"street_address": "65857 Ortiz Plains", '
        # '"secondary_address": "Suite 969", '
        # '"building_number": "979", "mail_box": "PO Box 312", '
        # '"community": "Summer Gardens", "zip_code": "51738-5712", '
        # '"zip": "39244-7001", "postcode": "87960-2311", '
        # '"time_zone": "America/New_York", "street_suffix": "Bridge", '
        # '"city_suffix": "bury", "city_prefix": "New", '
        # '"state": "Virginia", "state_abbr": "DE", '
        # '"country": "Israel", "country_code": "PS", '
        # '"latitude": 73.37310321416226, "longitude": 41.80257946317275, '
        # '"full_address": "Suite 349 66545 Junior Pike, Harveyville, NC 40350-4730"}'
    )

    do_nothing_stmt = insert_query.on_conflict_do_nothing(index_elements=["Vasyan"]).\
        returning(User)
    session.execute(do_nothing_stmt)
    session.commit()
    # user = session.query(User).where(User.name == "Vasyan").one()
    #
    # user_obj = user[0].json()
    # user_obj['coffee'] = user.coffee.to_json()
    # return jsonify(user_obj)
    return 'ok'


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

import json
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from models import User, Coffee
from cli import fill_db1

from loguru import logger


logger.debug("Simple logging.")

engine = create_engine('postgresql+psycopg2://user:pswd@localhost:5432/test')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


@logger.catch
def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("База создана")


# @logger.catch
# def add_user():
#     insert_query = insert(User).values(
#         id=11,
#         name="Vasyan",
#         has_sale=True,
#         coffee_id=5,
#         address='{"id": 9957, '
#         '"uid": "07790388-e8ed-4456-9f9b-9897f8fbbfc8", '
#         '"city": "Lake Evelin", '
#         '"street_name": "Christy Points", '
#         '"street_address": "65857 Ortiz Plains", '
#         '"secondary_address": "Suite 969", '
#         '"building_number": "979", "mail_box": "PO Box 312", '
#         '"community": "Summer Gardens", "zip_code": "51738-5712", '
#         '"zip": "39244-7001", "postcode": "87960-2311", '
#         '"time_zone": "America/New_York", "street_suffix": "Bridge", '
#         '"city_suffix": "bury", "city_prefix": "New", '
#         '"state": "Virginia", "state_abbr": "DE", '
#         '"country": "Israel", "country_code": "PS", '
#         '"latitude": 73.37310321416226, "longitude": 41.80257946317275, '
#         '"full_address": "Suite 349 66545 Junior Pike, Harveyville, NC 40350-4730"}'
#     )
#     do_nothing_stmt = insert_query.on_conflict_do_nothing(index_elements=["id"]). \
#             returning(User.name, User.coffee_id)
#     session.execute(do_nothing_stmt)
#     session.commit()
#     print("Добавление пользователя выполнено")

@logger.catch
def add_coffee():
    # coffee = insert(Coffee).values(id=1,
    #     title="titles",
    #                                origin="origin",
    #                                intensifier="intensifer",
    #                                notes="notes1 notes2")
    # coffe_stmt = coffee.on_conflict_do_nothing(index_elements=["id"]).returning(Coffee.title)
    # session.execute(coffe_stmt)
    # session.commit()
    coffee = Coffee(title="titles", origin="origin",
                    intensifier="intensifer", notes="notes1 notes2")
    session.add(coffee)
    session.commit()


@logger.catch
def read():
    users_list = []
    users = session.query(User).all()
    for user in users:
        user_obj = user.to_json()
        user_obj['coffee'] = user.coffee.to_json()
        users_list.append(user_obj)
        print(json.dumps(user_obj, indent=2))
        print("Вывод выполнен")




if __name__ == "__main__":
    create_db()

    # fill_db1()
    # add_user()
    read()
    # add_coffee()

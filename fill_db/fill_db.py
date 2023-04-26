import json
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Column, Sequence, Integer, String, Float, ForeignKey, Identity, Boolean, JSON
from sqlalchemy.orm import relationship
from typing import Dict, Any
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
from loguru import logger

from db_test import session, Base, engine


logger.debug("Simple logging.")


class BaseClass(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class Coffee(BaseClass):
    __tablename__ = 'coffee'

    title = Column(String(200), nullable=False)
    origin = Column(String(200))
    intensifier = Column(String(100))
    notes = Column(String())


class User(BaseClass):
    __tablename__ = 'users'

    name = Column(String(50), nullable=False)
    has_sale = Column(Boolean)
    address = Column(JSON)
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    coffee = relationship("Coffee", backref="users", lazy='joined')


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
    # users_list = []
    # users = session.query(User).all()
    # for user in users:
    #     user_obj = user.to_json()
    #     user_obj['coffee'] = user.coffee.to_json()
    #     users_list.append(user_obj)
    #     print(json.dumps(user_obj, indent=2))
    #     print("Вывод выполнен")

    coffee = session.query(Coffee).all()
    for c in coffee:
        print(c)


if __name__ == "__main__":
    create_db()




import json
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Column, Sequence, Integer, String, Float, ForeignKey, Identity, Boolean, JSON
from sqlalchemy.orm import relationship
from typing import Dict, Any
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
from loguru import logger

from models import Coffee, User
from db import engine, Base, session

logger.debug("Simple logging.")



def get_all_users():
    users_list = []
    users = session.query(User).all()
    for user in users:
        user_obj = user.to_json()
        user_obj['coffee'] = user.coffee.to_json()
        users_list.append(user_obj)

    print(json.dumps(users_list, indent=4))


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





if __name__ == "__main__":
    get_all_users()
    # add_user()
    # read()
    # add_coffee()

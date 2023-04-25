import json
import asyncio
import aiohttp
import random

from marshmallow import fields, post_load, EXCLUDE, Schema, INCLUDE
from flask.cli import FlaskGroup

from loguru import logger

from db import Base, engine, session
from app import app
from models import User, Coffee



number_of_records = 10
main_url_user = "https://random-data-api.com/api/v2/"
url_addres ="https://random-data-api.com/api/address/random_address"
url_coffee = "https://random-data-api.com/api/coffee/random_coffee"
nums_users = f"size={number_of_records}"
resource_user = "users"
response_type = "response_type=json"

url_user = f"{main_url_user}{resource_user}{'?'}{nums_users}{'&'}{response_type}"

logger.debug("Simple logging.")
# user_cli = AppGroup("user")
cli = FlaskGroup(app)


class UserSchema(Schema):

    first_name = fields.Str()
    last_name = fields.Str()

    class Meta:
        unknown = EXCLUDE

class CoffeeSchema(Schema):
    blend_name = fields.Str()
    origin = fields.Str()
    notes = fields.Str()
    intensifier = fields.Str()

    class Meta:
        unknown = EXCLUDE


@cli.command("create_db")
def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("База создана")


@cli.command("fill_db")
def fill_db():
    list_users = asyncio.run(get_users())
    list_address = asyncio.run(get_address())
    list_coffee = asyncio.run(get_coffee())
    add_data_in_db(list_users, list_address, list_coffee)

def fill_db1():
    list_users = asyncio.run(get_users())
    list_address = asyncio.run(get_address())
    list_coffee = asyncio.run(get_coffee())
    add_data_in_db(list_users, list_address, list_coffee)


@logger.catch
def add_data_in_db(users, address, coffee):
    for i_record in range(number_of_records):
        coffee_inst = Coffee()
        coffee_inst.title = coffee[i_record]["blend_name"]
        coffee_inst.notes = coffee[i_record]["notes"]
        coffee_inst.intensifier = coffee[i_record]["intensifier"]
        coffee_inst.origin = coffee[i_record]["origin"]
        session.add(coffee_inst)
    session.commit()
    for i_record in range(number_of_records):
        user = User()
        user.name = users[i_record]["first_name"] + " " + users[i_record]["last_name"]
        user.address = json.dumps(address[i_record])
        user.coffee_id = random.randint(1, number_of_records)
        user.has_sale = random.choice([True, False])
        session.add(user)
    session.commit()
    print("Добавление данных в базу выполнено")


@logger.catch
async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=50) as response:
            if response.status == 200:
                data = await response.json()
                # print(json.dumps(data, indent=4))
                return data


@logger.catch
async def get_users():
    "Формирует данные пользователей"

    data_user = await get_data(url_user)
    users_list = []
    for i in range(number_of_records):
        user = UserSchema().dump(data_user[i])
        users_list.append(user)

    return users_list



@logger.catch
async def get_address():
    "Формирует данные адресов пользователей"
    list_address = []
    records = 0
    while records < number_of_records:
        data_addres = await get_data(url_addres)
        list_address.append(data_addres)
        records += 1
    return list_address


@logger.catch
async def get_coffee():
    "Формирует данные о кофе"
    list_coffee = []
    records = 0
    while records < number_of_records:
        data = await get_data(url_coffee)
        data_coffee = CoffeeSchema().dump(data)
        list_coffee.append(data_coffee)
        records += 1
    return list_coffee


if __name__ == "__main__":
    cli()


# docker compose exec flask python cli.py create_db

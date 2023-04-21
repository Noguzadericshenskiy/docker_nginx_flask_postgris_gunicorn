import json
import asyncio
import aiohttp
import random
from marshmallow import fields, post_load, EXCLUDE, Schema, INCLUDE


number_of_records = 10
main_url_user = "https://random-data-api.com/api/v2/"
url_addres ="https://random-data-api.com/api/address/random_address"
url_coffee = "https://random-data-api.com/api/coffee/random_coffee"
nums_users = f"size={number_of_records}"
resource_user = "users"
response_type = "response_type=json"

url_user = f"{main_url_user}{resource_user}{'?'}{nums_users}{'&'}{response_type}"


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    first_name = fields.Str()
    last_name = fields.String()


class CoffeeSchema(Schema):
    blend_name = fields.Str()
    origin = fields.Str()
    notes = fields.Str()
    intensifier = fields.Str()

    class Meta:
        unknown = EXCLUDE


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            if response.status == 200:
                data = await response.json()
                print(json.dumps(data, indent=4))
                return data


async def get_users():
    "Формирует данные пользователей"
    try:
        data_user = await get_data(url_user)
        users_list = UserSchema().dump(data_user)
        return users_list
    except (SyntaxError, TimeoutError) as err:
        print(type(err), "::", err)


async def get_address():
    "Формирует данные адресов пользователей"
    list_address = []
    records = 0
    while records < number_of_records:
        data_addres = await get_data(url_addres)
        list_address.append(data_addres)
        records += 1
    return list_address


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

def main():
    list_users = get_coffee()
    list_address = get_address()
    list_coffee = get_coffee()



if __name__ == '__main__':
    main()



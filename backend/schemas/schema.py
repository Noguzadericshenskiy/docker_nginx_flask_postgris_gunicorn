from pydantic import BaseModel, Field
from typing import List, Dict


class BaseUser(BaseModel):
    name: str = Field(
        title='Название',
        description='Название')
    has_sale: bool = Field(
        title='Халява',
        description='Халява')
    address: Dict = Field(
        title='Адрес',
        description='Адрес')
    coffee_id: int = Field(
        title='ID coffee',
        description='ID coffee')


class UserIn(BaseUser):
    ...


class BaseCoffee(BaseModel):
    title: str = Field(title='Описание', description='Описание')
    origin: str = Field(
        title='Время приготовления',
        description='Время приготовления в минутах',
        )
    intensifier: str = Field(
        title='Ингредиенты',
        description='Ингредиенты')
    notes: list = Field(
        title='Нотки',
        description='Нотки')


class CoffeeIn(BaseCoffee):
    ...


class CoffeeOut(BaseCoffee):
    id: int = Field(title='ID Coffee')

    class Config:
        orm_mode = True


class UserOut(BaseUser):
    id: int = Field(title='ID User')
    coffee: CoffeeOut = Field(title='coffee')

    class Config:
        orm_mode = True
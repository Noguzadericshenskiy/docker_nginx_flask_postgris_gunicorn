from sqlalchemy import Column, Sequence, Integer, String, Float, ForeignKey, Identity, Boolean, JSON
from sqlalchemy.orm import relationship
from typing import Dict, Any

from db import Base


class BaseClass(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class Coffee(BaseClass):
    __tablename__ = 'coffee'
    # idi = Column(Integer, Sequence('id', start=1), primary_key=True)
    title = Column(String(200), nullable=False)
    origin = Column(String(200))
    intensifier = Column(String(100))
    notes = Column(String())


class User(BaseClass):
    __tablename__ = 'users'

    # id = Column(Integer, Sequence('id', start=1), primary_key=True)
    name = Column(String(50), nullable=False)
    has_sale = Column(Boolean)
    address = Column(JSON)
    coffee_id = Column(Integer, ForeignKey("coffee.id"))

    coffee = relationship("Coffee", backref="users", lazy='joined')


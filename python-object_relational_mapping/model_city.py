#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """Class City that inherits from State"""
    __tablename__ = "cities"
    id = Column(Integer,
                unique=True,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey("State.id"),
                      nullable=False)

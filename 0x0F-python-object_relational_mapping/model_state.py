#!/usr/bin/python3
""" contains State class and Base, an instance of declarative_base() """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class: with id and name attributes """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

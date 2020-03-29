#!/usr/bin/python3
""" db connection """
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class state(Base):
    """ Class state """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullabe=False, autoincrement="auto")
    name = Column(String(128), nullabe=False)

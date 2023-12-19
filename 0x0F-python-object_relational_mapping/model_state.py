#!/usr/bin/python3
"""now we will use sqlalchemy orm"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


md = MetaData()
Base = declarative_base()
class State(Base):
    """ a class that will be mapped by sqlalchemy"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)

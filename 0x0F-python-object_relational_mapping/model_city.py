#!/usr/bin/python3
"""create a new class city"""
from model_state import Base
from sqlalchemy import Column, String, Integer, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """the class of city"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

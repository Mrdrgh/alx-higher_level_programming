#!/usr/bin/python3
"""whatever"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    for inst in session.query(State).order_by(State.id):
        print(inst.id, inst.name, sep=": ")

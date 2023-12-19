#!/usr/bin/python3
"""a script to look for a state name ina sql table """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    inst = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(inst[0].id)
    except IndexError:
        print("Not found")

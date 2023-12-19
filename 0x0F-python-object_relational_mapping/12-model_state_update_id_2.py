#!/usr/bin/python3
"""alter a row in a sql table using sqlalchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker()
    sess = Session()
    instance = sess.query(State).filter(State.id == 2)
    instance[0].name = "New Mexico"
    sess.commit()

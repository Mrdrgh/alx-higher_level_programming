#!/usr/bin/python3
"""do inner joins with sqlalchemy"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    sss = Session()
    instace = sss.query(State.id, City.name,
                        City.state_id).filter(City.state_id == State.id)
    for isss in instace:
        print(isss[0] + ": (" + str(isss[1]) + ") " + isss[2])

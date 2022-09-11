#!/usr/bin/python3
"""Script that prints the State Object with the name passed as argument
from the database `hbtn_0e_6_usa`.
    Usage: ./10-model_state_my_get.py <MySQL username> <MySQL passwd>
                                      <db name> <State name query>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    isFound = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print(state.id)
            isFound = True
            break
    if isFound is False:
        print("Not found")

#!/usr/bin/python3
"""Script that deletes all State Objects with name containing an 'a' in
   hbtn_0e_6_usa
   Usage: ./13-model_state_delete_a.py <MySQL username> <MySQL passwd>
                                       <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()

#!/usr/bin/python3
"""Script that updates the State Object with id = 2 to name = New Mexico
   in the db `hbtn_0e_6_usa
   Usage: ./12-model_state_update_id_2.py <MySQL username> <MySQL passwd>
                                          <db>
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

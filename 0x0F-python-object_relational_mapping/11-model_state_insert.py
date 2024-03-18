#!/usr/bin/python3
"""Fetch all."""
import sys
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    st = State(name='Louisiana')
    s.add(st)
    s.commit()
    state = s.query(State).filter(
        State.name == 'Louisiana').first()
    print("{}".format(state.id))
    s.close()

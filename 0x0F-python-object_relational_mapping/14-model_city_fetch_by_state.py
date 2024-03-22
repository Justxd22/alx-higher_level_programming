#!/usr/bin/python3
"""Fetch all."""
import sys
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    for s, c in s.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    s.close()

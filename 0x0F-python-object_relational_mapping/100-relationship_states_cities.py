#!/usr/bin/python3
"""Calf from sanf."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    ns = State(name='California')
    nc = City(name='San Francisco')
    ns.cities.append(nc)
    s.add(ns)
    s.add(nc)
    s.commit()

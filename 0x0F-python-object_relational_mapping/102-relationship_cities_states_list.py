#!/usr/bin/python3
"""State from name."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City).order_by(City.id).all()
    for row in rows:
        print(f"{row.id}: {row.name} -> {row.state.name}")
    session.close()

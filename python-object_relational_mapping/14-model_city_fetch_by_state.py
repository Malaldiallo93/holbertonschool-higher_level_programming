#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    """Create an instance of SQLAlchemy engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))
    """Create a session to interact with the database"""
    session = Session(engine)
    """Retrieve all City objects along with their associated State objects"""
    cities_obj = session.query(State, City)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id)\
        .all()
    """Print results the City.name, State.id, State.name"""
    for state_row, cities_row in cities_obj:
        print(f"{state_row.name}: ({cities_row.id}) {cities_row.name}")

#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    """Create an instance of SQLAlchemy engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    """Create a session to interact with the database and Query"""
    session = Session(engine)
    """first() function"""
    states = session.query(State).first()

    if states is None:
        print("Nothing")
    else:
        print(f"{states.id}: {states.name}")

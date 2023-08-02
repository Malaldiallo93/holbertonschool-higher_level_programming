#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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
    """Create an object"""
    louisiana = State(name="Louisiana")
    """Create a session"""
    session = Session(engine)
    """Add object to the table"""
    session.add(louisiana)
    """Commit the change"""
    session.commit()

    print(louisiana.id)
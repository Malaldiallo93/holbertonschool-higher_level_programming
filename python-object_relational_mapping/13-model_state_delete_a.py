#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter a from hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    """Create an instance of SQLAlchemy engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))
    """Create a session"""
    session = Session(engine)
    """filter() with like("%a%")"""
    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    """Delete object with a in it"""
    for row in states:
        session.delete(row)
    """Commit change"""
    session.commit()

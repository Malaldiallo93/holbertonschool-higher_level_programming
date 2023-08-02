#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

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
    """Execute Object"""
    my_row = session.execute(select(State).filter_by(id=2)).scalar_one()
    """Update Object"""
    my_row.name = "New Mexico"
    """Commit change"""
    session.commit()
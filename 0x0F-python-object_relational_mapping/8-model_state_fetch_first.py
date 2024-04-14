#!/usr/bin/python3
"""
Module that query the first object
of the secondury class
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    """
    create a session"""
    session = sessionmaker(bind=engine)
    session = session()
    """
    create a query"""
    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))

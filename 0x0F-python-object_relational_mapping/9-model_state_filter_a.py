#!/usr/bin/python3
"""
Module
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import func


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], "hbtn_0e_6_usa"),
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)
    Session = session()
    """
    query State"""
    result = Session.query(State).filter(func.lower(State.name).like('%a%'))
    for state in result:
        print("{}: {}".format(state.id, state.name))

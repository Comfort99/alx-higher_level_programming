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
    Session = sessionmaker(bind=engine)
    session = Session()
    """
    query State"""
    result = session.query(State).filter(
        func.lower(State.name).like('%a%')).all()

    for state in result:
        session.delete(state)
    session.commit()

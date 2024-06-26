#!/usr/bin/python3
"""
Module
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
    session = sessionmaker(bind=engine)
    session = session()
    """
    create query"""
    name = session.query(State).filter(State.name == sys.argv[4]).first()
    if name:
        print(name.id)
    else:
        print("Not found")

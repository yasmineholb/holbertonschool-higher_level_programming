#!/usr/bin/python3
""" db connection """
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    se = session.query(State).filter_by(id=4).first()
    se.name = 'New Mexico'
    session.add(se)
    session.commit()
    session.close()

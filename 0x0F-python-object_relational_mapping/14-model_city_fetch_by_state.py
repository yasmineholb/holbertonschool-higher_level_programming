#!/usr/bin/python3
""" db connection """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    se = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id.asc()).all()
    for s, c in se:
        print("{}: ({}) {}".format(c.name, s.id, s.name))
    session.close()

#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    usrname = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(usrname, pswd, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    sttfilter = query.filter(State.name.like('%a%')).order_by(State.id).all()

    for state in sttfilter:
        print("{}: {}".format(state.id, state.name))

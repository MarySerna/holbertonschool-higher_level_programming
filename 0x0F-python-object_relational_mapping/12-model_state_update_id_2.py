#!/usr/bin/python3
"""
Script that changes the name of a State object from the database
hbtn_0e_6_usa
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
                           .format(usrname, pswd, dbname, pool_pre_ping=True))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    state2 = query.filter(State.id == 2).all()

    if state2:
        state2[0].name = "New Mexico"
    session.commit()
    session.close()

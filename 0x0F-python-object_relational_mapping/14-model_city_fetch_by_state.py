#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    usernm = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(usernm, password, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City)
    stfilter = query.filter(City.state_id == State.id).all()

    for state, city in stfilter:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

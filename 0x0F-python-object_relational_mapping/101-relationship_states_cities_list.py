#!/usr/bin/python3
""" Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    database_url = 'mysql://{}:{}@localhost:3306/{}'.\
                    format(argv[1], argv[2], argv[3])
    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in s:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()

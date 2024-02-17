#!/usr/bin/python3
""" Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    database_url = 'mysql://{}:{}@localhost:3306/{}'.\
                    format(argv[1], argv[2], argv[3])
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()

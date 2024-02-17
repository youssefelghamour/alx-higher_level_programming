#!/usr/bin/python3
""" Script that prints all City objects from the database hbtn_0e_14_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
from sys import argv


if __name__ == '__main__':
    database_url = 'mysql://{}:{}@localhost:3306/{}'.\
                    format(argv[1], argv[2], argv[3])
    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in result:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()

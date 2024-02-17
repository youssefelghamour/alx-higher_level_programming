#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    database_url = 'mysql://{}:{}@localhost:3306/{}'.\
                    format(argv[1], argv[2], argv[3])
    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like(argv[4])).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # mysql username, password, database name
    user = argv[1]
    password = argv[2]
    db = argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

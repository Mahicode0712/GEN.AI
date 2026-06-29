from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./items.db"

#engine-->it's the connection to the db file
engine = create_engine(DATABASE_URL,
    connect_args = {"check_same_thread": False})

#creates individual DB sessions
SessionLocal = sessionmaker(autocommit = False,
     autoflush = False, bind = engine)

Base = declarative_base()

#fastapi dependency - yields a session,then closes it
def get_db():
    db = SessionLocal()
    try:
        yield db  #<-- Depends() picks this up
    finally:
        db.close()    
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:2609@localhost:5432/furniture', echo=True)
Base = declarative_base()
session = sessionmaker()
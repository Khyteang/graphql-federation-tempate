import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

metadata = MetaData()
Base = declarative_base(metadata=metadata)

load_dotenv(".env")
DATABASE_URL = os.environ["DATABASE_URL"]

ENGINE = create_engine(DATABASE_URL)


db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))
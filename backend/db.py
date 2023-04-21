import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL", "sqlite://"))
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

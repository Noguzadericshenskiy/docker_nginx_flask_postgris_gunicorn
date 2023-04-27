import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

user = os.getenv("USER_DB")
password = os.getenv("PASSWORD_DB")
name = os.getenv("NAME_DB")
host = 'database'
port = "5432"

# URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
URL = "postgresql+psycopg2://user:pswd@localhost:5432/test"

# engine = create_engine(os.getenv("DATABASE_URL", "sqlite://"))
engine = create_engine(URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

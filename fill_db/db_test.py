from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql+psycopg2://user:pswd@localhost:5432/test')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

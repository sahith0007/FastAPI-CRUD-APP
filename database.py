from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Create Engine DataBase
engine = create_engine("mysql+pymysql://root@localhost:3306/test")

Base = declarative_base()

SessionLoacal = sessionmaker(bind=engine, expire_on_commit=False)

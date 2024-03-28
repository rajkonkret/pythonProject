# ORM - działanie z bazą danych w sposób obiektów poprzez bibliotekę
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# encja - klasa odzwierciedlająca tabele w bazie danych
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine('sqlite:///my_database_alch.db')
Base.metadata.create_all(engine)

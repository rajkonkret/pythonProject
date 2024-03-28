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

    def __repr__(self):
        return f"{self.id} {self.name}"


# echo=True - dodatkowe logi
engine = create_engine('sqlite:///my_database_alch.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesion = Session()

new_uer = User(name="Jan Kowalski", age=30)
sesion.add(new_uer)  # INSERT INTO users (name, age) VALUES (?, ?)

sesion.commit()
sesion.close()

users = sesion.query(User).all()
for user in users:
    print(user)
    # print(user.name)
# Po dodaniu __repr__
# 1 Jan Kowalski
# 2 Jan Kowalski
# 3 Jan Kowalski
# 4 Jan Kowalski
# 5 Jan Kowalski
# 6 Jan Kowalski

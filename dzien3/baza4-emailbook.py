from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# engine = create_engine('sqlite:///:memory:')  # baza danych w pamięci
engine = create_engine('sqlite:///emailbook.db')  # baza danych w pamięci
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship('Address',
                             back_populates='person',
                             order_by='Address.email',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


# tworzenie tabel w bazie
Base.metadata.create_all(engine)

# tworzenie sesji do poruszania i komunikowania się z bazą
Session = sessionmaker(bind=engine)
session = Session()

# wypełnianie bazy danymi
anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi", age=45)

obi.addresses = [
    Address(email='obi@example,com'),
    Address(email='waka@wp.pl')
]
vader = Person(name='Lord Vader', age=59)
vader.addresses = [
    Address(email='vader@vader.com'),
    Address(email='vader@starwars.pl')
]
# session.add(anakin)
# session.add(obi)
session.add(vader)

session.commit()
session.close()

# odczyt danych z bazy
all_ = session.query(Person).all()
print(all_)
# [Anakin (id=1), Obi (id=2), Lord Vader (id=3), Lord Vader (id=4)]

an1 = session.query(Person).first()
print(an1)  # Anakin (id=1)

vader_list = session.query(Person).filter(
    Person.name.like('Lord%')
).all()
print(vader_list)  # [Lord Vader (id=3), Lord Vader (id=4)]

for o in vader_list:
    print("id=", o.id, 'name:', o.name, "age:", o.age, 'email:', o.addresses)
# [Anakin (id=1), Obi (id=2), Lord Vader (id=3), Lord Vader (id=4)]
# Anakin (id=1)
# [Lord Vader (id=3), Lord Vader (id=4)]
# id= 3 name: Lord Vader age: 59 email: [vader@starwars.pl, vader@vader.com]
# id= 4 name: Lord Vader age: 59 email: [vader@starwars.pl, vader@vader.com]

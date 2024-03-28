from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///book_shop.db')  # baza danych w pamięci
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship('Publisher', back_populates='books')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_author = Author(name="Adam Mickiewicz")
new_publisher = Publisher(name="Wydawnictwo XYZ")
new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)

# session.add_all(
#     [new_author, new_publisher, new_book]
# )

session.commit()
session.close()

authors = session.query(Author).all()
print(authors)
# [<__main__.Author object at 0x0000020B4C26B260>,
# <__main__.Author object at 0x0000020B4C26BFB0>,
# <__main__.Author object at 0x0000020B4C2C8E90>]

for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        print(f"Ksiązka {b.title}, Wydawca {b.publisher.name}")
print("------")

publishers = session.query(Publisher).all()
for p in publishers:
    print(f"Wydawca: {p.name}")
    for b in p.books:
        print(f"Ksiązka {b.title}, Author: {b.author.name}")
#
# Author: Adam Mickiewicz
# Ksiązka Pan Tadeusz, Wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Ksiązka Pan Tadeusz, Wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Ksiązka Pan Tadeusz, Wydawca Wydawnictwo XYZ
# ------
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz, Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz, Author: Adam Mickiewicz
# Wydawca: Wydawnictwo XYZ
# Ksiązka Pan Tadeusz, Author: Adam Mickiewicz

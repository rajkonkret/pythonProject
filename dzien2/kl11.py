import pickle
from dataclasses import dataclass
from kl10 import Person

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int


with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)

# Person(first_name='Maciek', last_name='Nowak', id=1)
# Person(first_name='Tomek', last_name='Kowalski', id='2')
# [Person(first_name='Maciek', last_name='Nowak', id=1), Person(first_name='Tomek', last_name='Kowalski', id='2')]
# [Person(first_name='Maciek', last_name='Nowak', id=1), Person(first_name='Tomek', last_name='Kowalski', id='2')]

# Po dodaniu main w kl10 tylko wyswietli dane z tego pliku
# [Person(first_name='Maciek', last_name='Nowak', id=1), Person(first_name='Tomek', last_name='Kowalski', id='2')]
for person in p:
    print(f"id={person.id}, name={person.first_name}")

# id = 1, name = Maciek
# id = 2, name = Tomek

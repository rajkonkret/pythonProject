from dataclasses import dataclass
import pickle


# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int


p1 = Person("Maciek", "Nowak", 1)
print(p1)
# <__main__.Person object at 0x000001757809D370>
# po uzyciu @dataclass
# Person(first_name='Maciek', last_name='Nowak', id=1)

p2 = Person("Tomek", "Kowalski", "2")  # Person(first_name='Tomek', last_name='Kowalski', id='2')
print(p2)

people = [p1, p2]
print(people)
# [Person(first_name='Maciek', last_name='Nowak', id=1), Person(first_name='Tomek', last_name='Kowalski', id='2')]

with open('dane.pickle', 'wb') as stream:
    pickle.dump(people, stream)

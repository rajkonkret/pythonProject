import requests
from pydantic import BaseModel
from typing import List

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)
# <Response [200]> ok
# 3xx - błedy przekierowania
# 4xx - błedy klienta np 404 - błedny adres, 400 Bad Request
# 5xx - błedy po stronie serwera

print(response.text)

data = response.json()
print(type(data))
print(data)

for i in data:
    print(i)
# message
# people
# number

print(data['people'])


# [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#  {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#  {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#  {'name': "Loral O'Hara", 'craft': 'ISS'}]


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int
    # number: str


# pydantic_core._pydantic_core.ValidationError: 1 validation error for AstroData
# number

data = AstroData(**response.json())
print(data)
# message = 'success'
# people = [Astronaut(name='Jasmin Moghbeli', craft='ISS'), Astronaut(name='Andreas Mogensen', craft='ISS'),
#           Astronaut(name='Satoshi Furukawa', craft='ISS'), Astronaut(name='Konstantin Borisov', craft='ISS'),
#           Astronaut(name='Oleg Kononenko', craft='ISS'), Astronaut(name='Nikolai Chub', craft='ISS'),
#           Astronaut(name="Loral O'Hara", craft='ISS')]
# number = 7

print(data.people)
print(data.people[0].name)  # Jasmin Moghbeli

people = data.people
for p in people:
    print(p)  # name="Loral O'Hara" craft='ISS'

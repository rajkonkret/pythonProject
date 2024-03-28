from pydantic import BaseModel
import requests as re

url = 'https://randomuser.me/api/'
response = re.get(url)
print(response.text)
data = response.json()
print(data)
user = data['results'][0]
print(f"Imię: {user['name']['first']}")
print(f"Nazwisko: {user['name']['last']}")
print(f"Email: {user['email']}")

photo_url = user['picture']['large']


class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture


user_info = UserInfo(**user)
print(user_info)
# name = Name(title='Mr', first='Jonathan', last='Andersen')
# email = 'jonathan.andersen@example.com'
# picture = Picture(large='https://randomuser.me/api/portraits/men/51.jpg')

photo_url_pydantantic = user_info.picture.large
resp = re.get(photo_url_pydantantic)
with open("user_photo.jpg", 'wb') as f:
    f.write(resp.content)

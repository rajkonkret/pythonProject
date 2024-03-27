# słownik
# __missing__ - metoda wykonywana, gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


# słownik dopuszczający wywołanie kluczy nie uwzględniając duże/małe litery
class CaseInensitiveDict(dict):
    def __missing__(self, key):
        # return self.get(key.lower)
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}
# d_python['name']  #
d1 = DefaultDict()
print(d1['name'])  # default
d1['name'] = 'Radek'
print(d1)
d1['imie'] = "Zenek"
print(d1)  # {'name': 'Radek', 'imie': 'Zenek'}
print(type(d1))  # <class '__main__.DefaultDict'>

d2 = AutoKeyDict()
print(d2)  # {}
print(d2['imie'])  # imie
print(d2)  # {'imie': 0}

d3 = CaseInensitiveDict()
d3['name'] = "Radek"
print(d3['NaME'])  # Radek

# dziedziczenie
class Contact:
    all_contacts = []  # pusta lista, wspolna dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):  # __repr__ nadpisze __str__
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):  # dziedziczymy po klasie Contact
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin2@wp.pl")
c3 = Contact("Tomek", "admin3@wp.pl")
print(c1)
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek admin2@wp.pl, Tomek admin3@wp.pl]

s1 = Suplier("Tomasz", "tomasz@onet.pl")
print(s1)
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek admin2@wp.pl, Tomek admin3@wp.pl, Tomasz tomasz@onet.pl]
# po dodaniu !r w __repr__ dodaje cudzysłowy
# ['Adam' 'admin@wp.pl', 'Radek' 'admin2@wp.pl', 'Tomek' 'admin3@wp.pl', 'Tomasz' 'tomasz@onet.pl']
s1.order("Kawa")  # Kawa zamówiono od Tomasz

from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # pusta lista naszego typu

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.email}"


class Suplier(Contact):  # dziedziczymy po klasie Contact
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return "suplier"


class Friend(Suplier):
    def __init__(self, name, mail, phone):
        super().__init__(name, mail)  # super() - klasa nadrzędna -musi wywołąć w konstruktorze
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.email} +48 {self.phone}"


c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "mietekpl@wp.pl")
c3 = Contact("Mietek", "zolza@wp.pl")
print(Contact.all_contacts)
# [Contact Adam adam@wp.pl, Contact Radek mietekpl@wp.pl, Contact Mietek zolza@wp.pl]
s1 = Suplier("Zenek", "qqq@wp.pl")
print(Contact.all_contacts)
# [Contact Adam adam@wp.pl, Contact Radek mietekpl@wp.pl, Contact Mietek zolza@wp.pl, suplier]
f1 = Friend("Tomek", "abc@wp.pl", "123456789")
print(Contact.all_contacts)
# [Contact Adam adam @ wp.pl,
#  Contact Radek mietekpl @ wp.pl,
#  Contact Mietek zolza @ wp.pl,
#  suplier,
#  Friend Tomek abc @ wp.pl + 48 123456789]
print(Friend.__mro__)  # kolejnośc rozwiązywania nazw przy obiektach
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f1.order("frytki")  # frytki zamówiono od Tomek

pprint(Contact.all_contacts)
# [Contact Adam adam@wp.pl,
#  Contact Radek mietekpl@wp.pl,
#  Contact Mietek zolza@wp.pl,
#  suplier,
#  Friend Tomek abc@wp.pl +48 123456789]

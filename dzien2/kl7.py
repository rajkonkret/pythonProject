# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z kalsy B")


class C(B, A):
    """
    Klasa dziedziczy po kalsach A i B
    """


a = A()
b = B()
a.method()  # Metoda z klasy A
b.method()  # Metoda z kalsy B

c = C()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
c.method()  # Metoda z kalsy B


class D(A, B):  # kolejnosc ma znaczenie  zpunktu widzenia __mro__
    """
    Klasa
    """


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(B, A):
    def method(self):
        A.method(self)  # wskazanie, ze ma byc wykonana z klasy A


f = F()
f.method()  # Metoda z klasy A


class G(A, B):
    def method(self):
        super().method()  # wykonanie method z klasy A
        print("Dopisane")


g = G()
g.method()
# Metoda z klasy A
# Dopisane

print(G.__mro__)
# (<class '__main__.G'>, < class '__main__.A' >, < class '__main__.B' >, < class 'object' > )

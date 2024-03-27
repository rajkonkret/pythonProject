# klasa - szablon
# pola
# funkcje
# z klasy tworzymy obiekty tzw instancje
# paradygmaty: dziedziczenie, hermetezacja(enkapsulacja), polimorfizm, abstrakcja

import math


# do zastosowań związanych z matematką

# definicja klasy
class MyFirstClass:
    """
    Klasa w Pythonie, reprezentująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0) -> None:
        """
        metoda inicjalizująca (tzw. konstruktor)
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: float, y: float) -> None:  # to są tylko podpowiedzi
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # odpowiada za wyswietlenie obiektu
        return f"(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"REPR(x={self.x}, y={self.y})"


p1 = MyFirstClass()
print(MyFirstClass.__doc__)  # wypisanie dokumentacji
print(p1)  # <__main__.MyFirstClass object at 0x000001BC012C3D40>

p2 = MyFirstClass(10, 10)
print(p2)
# (x=0, y=0)
# (x=10, y=10)
p1.move(50, 50)
# p1.move("50", "50")
print(p1.calculate(p2))  # 56.568542494923804
print(p1)
p1.reset()
print(p1)
# (x=0, y=0)  __str__
lista = [p1, p2]
print(lista)
# [<__main__.MyFirstClass object at 0x000002AAD2D3DF10>,
# <__main__.MyFirstClass object at 0x000002AAD2D3DEE0>]
# [REPR(x=0, y=0), REPR(x=10, y=10)] __repr__

# abstrakcja - klasa dla której nie można utworzyc obiektu
# tworzy się aby wymusic polimorfizm przy klasach dziedziczących
from abc import ABC, abstractmethod


# Po oznaczeniu klasy i metody jako abstrakcyjne nie da się utworzyć obiektu tej klasy
# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod
    def drukuj(self):
        pass

    @staticmethod  # metoda statyczna - nie potrzebuje obiektu do działąnia
    def from_string():  # bez self
        print("Metoda statyczna")

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może przekroczyc maksimum")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje...", self.values)


# nie da się utworzyć obiektu tej klasy bo nie implementuje metody
# abstrakcyjnej drukuj()
class NewCounter(Counter):
    """
    Licznik bez metody drukuj()
    """


# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c = Counter()
# c.increment()
# print(c.values)
# c.drukuj()

bc = BoundedCounter(10)
bc.increment()
bc.drukuj()  # Drukuje... 11

# nc = NewCounter()
# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'

# Użycie metody statycznej
Counter.from_string()  # Metoda statyczna
# Counter.drukuj()  # TypeError: Counter.drukuj() missing 1 required positional argument: 'self'

e = BoundedCounter.from_counter(bc)
e.drukuj()  # Drukuje... 11

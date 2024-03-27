# hermetezycja, enkapsulacja

class Boat:
    """
    Dokumentacja klasy
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole prywatne

    def sail(self):
        self.__speed += 10

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")

    def break_(self):
        self.__private()
        self.__speed -= 10

    def __private(self):  # metoda prywatna
        print("Private")


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
b1.sail()
b1.sail()
# po oznaczeniu pola jako prywtnie nie jest dostępne z poza kalsy
# print(b1.__speed)  # AttributeError: 'Boat' object has no attribute '__speed'
b1.speedometer()  # Speed in knots 50
b1.break_()
b1.break_()
b1.speedometer()  # Speed in knots 30
b1.__speed = 0
print(b1.__speed)  # to jest pole publiczne, przypadkowo o tej samej nazwie
b1.speedometer()
# 0
# Speed in knots 30

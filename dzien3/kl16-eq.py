# __eq__ porównanie (==)
# __lt__ mniejsze (<)
# __gt__ większe (>)
from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


@total_ordering  # dostarcza pozostałe metody porównania
class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        """Porównuje obiekty po wartośi value"""
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num1 = MyNumber(5)
num2 = MyNumber(15)
# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)

num3 = MyNumber2(5)
num4 = MyNumber2(15)
print(num3 < num4)

num5 = MyNumber2(15)
print(num5 == num4)
# True
# True
# True
print(num3 > num5)

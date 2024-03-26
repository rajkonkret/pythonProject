# generatory - sekwencyjnie zwraca wyniki operacji(jeden po drugim)
# zapamiętuje gdzie zakończył
# pomaga lepiej wykorzystac pamiec i zasoby systemu

def kwadrat(n):
    for x in range(n):  # 0...n-1  range(5) -> 0..4
        print(x ** 2)  # potega 2 liczby


# ctrl alt l - porządkowanie kody wg zasad PEP8
kwadrat(5)


def kwadrat2(n):
    for x in range(n):  # pamieta wartość na której zakończył(pozycje)
        yield x ** 2  # zwraca wartosc i przestawia wskaźnik na nastepny


print(kwadrat2(5))  # <generator object kwadrat2 at 0x000001AB869F3780>
kwa = kwadrat2(5)  # przypisanie generatora do zmiennej
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(next(kwa))
try:
    print(next(kwa))  # StopIteration - bład gdy wyczerpiemy generator
    print(next(kwa))
except StopIteration:
    print("Generator zakończył działanie")

for i in kwadrat2(5):
    print(i)

print(list(kwadrat2(5)))  # [0, 1, 4, 9, 16]

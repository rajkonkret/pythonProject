# funkcje lambda - skrócony zapis funkcji
# mozliwosc deklaracji funkcji w miejscu uzycia
# funkcja anonimowa - nie ma nazwy

def liczymy(x, y):
    return x * y


print(liczymy(5, 9))

liczymy2 = lambda x, y: x * y
print(liczymy2(7, 8))

lista = [1, 2, 3, 4, 5, 6, 7, 20, 55, 100, 200]

# petla i zapis do listy
# jednolinijkowo petla
# zrobic funkcje co zmienia dane i uzyc jej w peli, wyniki zapisac do listy
lista2 = []
for i in lista:
    lista2.append(i * 2)
print(lista2)  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 400]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 400]


def zmien(x):
    return x * 2


# funkcje wyzszego rzedu
# map() - bierze element, wykonuje na nim funkcje i zwraca wynik
print(f"Użycie map(): {list(map(zmien, lista))}")  # Użycie map(): [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 400]
# mozliwośc uzycia lambdy jako funkcji anonimowej
print(f"Użycie map() i lambda: {list(map(lambda x: x * 2, lista))}")
# Użycie map() i lambda: [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 400]

# filtrowanie danych
# filter() - filtruje dane wg zadanej funkcji, zwraca spełniające warunek
print(f"Uzycie filter() {list(filter(lambda x: x > 3, lista))}")  # Uzycie filter() [4, 5, 6, 7, 20, 55, 100, 200]
#  x > 50
# x > 5 and x < 67
print(f"Uzycie filter() {list(filter(lambda x: x > 50, lista))}")  # Uzycie filter() [55, 100, 200]

print(f"Uzycie filter() {list(filter(lambda x: x > 5 and x < 67, lista))}")  # Uzycie filter() [6, 7, 20, 55]
print(f"Uzycie filter() {list(filter(lambda x: 5 < x < 67, lista))}")  # Uzycie filter() [6, 7, 20, 55]

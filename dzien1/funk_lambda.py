# funkcje lambda - skrócony zapis funkcji
# mozliwosc deklaracji funkcji w miejscu uzycia
# funkcja anonimowa - nie ma nazwy
from functools import reduce


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

r0 = {"miasto": "Kielce"}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault('ZIP', "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)
print(lata)  # [(2000, 29.7), (2001, 33.12), (2010, 32.92)]


# ctrl d - powielenie linii
# ctrl / - komentowanie kodu
# ctrl alt l - formatowanie kodu

def iloczyn(a, b):
    return a * b


def suma(a, b):
    return a + b


liczby = [1, 2, 3, 4, 5]
wynik = reduce(iloczyn, liczby)  # 120
print(wynik)
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
print(reduce(suma, liczby))  # 15
# 1 + 2 = 3
# # 3 + 3 = 6
# # 6 + 4 = 10
# # 10 + 5 = 15
print(reduce(lambda a, b: a + b, liczby))  # 15

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)  # stworzenie iteratoa na danych z listy
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

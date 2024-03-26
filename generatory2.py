import sys

generator_1 = [x for x in range(5)]
print(generator_1)  # [0, 1, 2, 3, 4]
# [] - lista
# {} - słownik, set
# () - tupla (krotka)
# to jest generator nawiasy ()
generator2 = (x for x in [1, 2, 3, 4, 5])
print(type(generator2))  # <class 'generator'>
print(next(generator2))
print(next(generator2))
print(next(generator2))


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * i
        i += i


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fi = fibo()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(sys.int_info)


# sys.int_info(bits_per_digit=30
#              , sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fibo2 = fibo_with_index(10)
print(next(fibo2))
print(next(fibo2))
print(next(fibo2))
print(next(fibo2))
print(next(fibo2))  # (4, 3)

for i in fibo_with_index(10):
    print(f"Element {i}")  # f-string, w {} mozemy wstawiac wartośc np.: zmiennej
# Element (8, 21)
a, b = (8, 21)
print(a)
print(b)

for i, n in fibo_with_index(10):
    print(f"Element {i}, wartość {n}")  # Element 9, wartość 34

a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3]


def counter(start=0):
    n = start
    while True:
        result = yield n  # do result trafia komunikaty wysłane jako send, gdy nie ma przyjmie wartość None
        print(result)
        n += 1
        if result == 'q':
            break


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(c.send("OK"))  # OK
try:
    print(c.send("q"))  # wysyłamy komunikat do generatora
except StopIteration as e:
    print("Generator zakończył działanie", e)
# print(next(c))  #
d = counter(10)
print(next(d))

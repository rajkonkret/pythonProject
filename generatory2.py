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

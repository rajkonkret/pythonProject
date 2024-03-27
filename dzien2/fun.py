def example(a, b, /, d=0, **kwargs):  # argumenty słownikowe
    print("a, b", a, b)
    print("d", d)
    print("kwargs", kwargs)


example(1, 3)
example(1, 2, 3)  # d 3
example(1, 3, d=8)  # d 8

# / - oddziela parametry, które obowiązkowo muszą byc przekazane po pozycji
# od parametrów, które mogą być przekazane po nazwie
# example(b=9, a=9, d=10)  # TypeError: example() missing 2 required positional arguments: 'a' and 'b'
example(1, 2, 3, a=9, b=7)  # kwargs {'a': 9, 'b': 7}


# * - dowolna ilosc argumentów pozycyjnych
# ** - dowlona ilość argumentów nazwanych
def all_params(*args, **kwargs):
    pass


all_params(1, 2, 3, 4, 5, 6, a=8, b=0, n=7, name="Radek")

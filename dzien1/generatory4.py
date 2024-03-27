# stworzenie raportu, przetworzenie danych, dane generowane generatorem


def generator_danych(dane):
    for element in dane:
        yield element


# % 2 modulo - reszta z dzielenia
def przetworz_dane(dane):
    przetworzone_dane = [element for element in dane if element % 2 == 0]
    return przetworzone_dane


def stworz_raport(dane):
    for elemnent in generator_danych(dane):
        print(f"Raport został utworzony dla elemntu: {elemnent}")


dane = range(100_000)
prz_dane = przetworz_dane(dane)
stworz_raport(prz_dane)

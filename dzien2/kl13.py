# własne wyjątki tworzymy poprzez klasę dziedziczącą po Exception

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę cąlkowita"))
    if x < 0:
        raise MyException("Liczba musi być dodatnia")
except MyException as e:
    print("Wystąpił wyjątek MyException", e)
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # wyjkona się gdy nie ma błedu
    print(f"Wprowadziłęś poprawną wartośc {x}")
finally:  # wykonuje się zawsze
    print("Dane zostały wprowadzony")

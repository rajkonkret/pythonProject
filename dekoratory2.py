def upercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@upercase_decorator
def greeting():
    return "Hallo World!"


print(greeting())
# dekorator co robi bold(pogrubienie)
name = "Radek"
name.upper()  # """ Return a copy of the string converted to uppercase. """
print(name)  # Radek
print(name.upper())  # RADEK
# print("A" + 5)  # TypeError: can only concatenate str (not "int") to str
print("A" + str(5))  # A5 - konkatenacja
# silne typowanie - nie zamiania typów automatycznie
# musimy jawnie pokazac co cchemy zrobic
# print("5" + 5)
print(int("5") + 5)  # 10

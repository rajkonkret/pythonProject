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

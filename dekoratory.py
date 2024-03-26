# dekorator - opakowuje funkcje w inna funkcjonalnosc
# wykorzystuje zasdday funkcji zagnieżdzonej, wewnętrznej

def fun1():
    print("To jest fun1")

    def fwew(a, b):
        return a * b

    return fwew  # zwracamy adres funkcji, referencje


print(fun1())  # <function fun1.<locals>.fwew at 0x0000010D736098A0>
xFun = fun1()
print(type(xFun))  # <class 'function'>
xFun(4, 5)

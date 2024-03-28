# bład zaokrąglenia float
import sys
from decimal import Decimal

print(0.1 + 0.2)  # 0.30000000000000004
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# Decimal - typ danych do ominięcia problemu liczb float
kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
print(kwota1 < kwota2)  # __lt__ False
precyzja = Decimal('0.00')

# dodawanie kwot
suma = kwota2 + kwota1
print("Suma:", suma)

# różnica
roznica = kwota1 - kwota2
print("Różnica:", roznica)
print("Różnica:", roznica.quantize(precyzja))

# mnozenie
podatek = Decimal(0.23)
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))
# Kwota z podatkiem: 12.60750000000000010241807403
# Kwota z podatkiem: 12.61

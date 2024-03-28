import xml.etree.ElementTree as ET
import requests as re
from pydantic import BaseModel
from typing import List


class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRatesTable(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'
response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")

data = root.find(".//EffectiveDate").text
print(f"Data tabeli: {data}")
# Tabela: A
# Data tabeli: 2024-03-28

no = root.find(".//No").text
rates = root.findall('.//Rate')

currency_rates = []
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = float(rate.find('Mid').text)
    print(f"Currency {currency}, Code {code}, Mid {mid}")
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=mid))

exchange_rate_table = ExchangeRatesTable(table=table_name, date=data, number=no, rates=currency_rates)
print(exchange_rate_table)
# table = 'A'
# date = '2024-03-28'
# number = '063/A/NBP/2024'
# rates = [CurrencyRate(currency='bat (Tajlandia)', code='THB', mid=0.1099),
#          CurrencyRate(currency='dolar amerykański', code='USD', mid=4.0081),
#          CurrencyRate(currency='dolar australijski', code='AUD', mid=2.6005),
#          CurrencyRate(currency='dolar Hongkongu', code='HKD', mid=0.5123),
#          CurrencyRate(currency='dolar kanadyjski', code='CAD', mid=2.9447),
#          CurrencyRate(currency='dolar nowozelandzki', code='NZD', mid=2.3884),
#          CurrencyRate(currency='dolar singapurski', code='SGD', mid=2.967),
#          CurrencyRate(currency='euro', code='EUR', mid=4.3191),
#          CurrencyRate(currency='forint (Węgry)', code='HUF', mid=0.010912),
#          CurrencyRate(currency='frank szwajcarski', code='CHF', mid=4.4228),
#          CurrencyRate(currency='funt szterling', code='GBP', mid=5.0474),
#          CurrencyRate(currency='hrywna (Ukraina)', code='UAH', mid=0.1021),
#          CurrencyRate(currency='jen (Japonia)', code='JPY', mid=0.026472),
#          CurrencyRate(currency='korona czeska', code='CZK', mid=0.1705),
#          CurrencyRate(currency='korona duńska', code='DKK', mid=0.5792),
#          CurrencyRate(currency='korona islandzka', code='ISK', mid=0.028737),
#          CurrencyRate(currency='korona norweska', code='NOK', mid=0.3693),
#          CurrencyRate(currency='korona szwedzka', code='SEK', mid=0.3741),
#          CurrencyRate(currency='lej rumuński', code='RON', mid=0.8685),
#          CurrencyRate(currency='lew (Bułgaria)', code='BGN', mid=2.2083),
#          CurrencyRate(currency='lira turecka', code='TRY', mid=0.1233),
#          CurrencyRate(currency='nowy izraelski szekel', code='ILS', mid=1.0875),
#          CurrencyRate(currency='peso chilijskie', code='CLP', mid=0.004091),
#          CurrencyRate(currency='peso filipińskie', code='PHP', mid=0.0711),
#          CurrencyRate(currency='peso meksykańskie', code='MXN', mid=0.2416),
#          CurrencyRate(currency='rand (Republika Południowej Afryki)', code='ZAR', mid=0.21),
#          CurrencyRate(currency='real (Brazylia)', code='BRL', mid=0.8028),
#          CurrencyRate(currency='ringgit (Malezja)', code='MYR', mid=0.8468),
#          CurrencyRate(currency='rupia indonezyjska', code='IDR', mid=0.0002528),
#          CurrencyRate(currency='rupia indyjska', code='INR', mid=0.048059),
#          CurrencyRate(currency='won południowokoreański', code='KRW', mid=0.002964),
#          CurrencyRate(currency='yuan renminbi (Chiny)', code='CNY', mid=0.5543),
#          CurrencyRate(currency='SDR (MFW)', code='XDR', mid=5.2912)]
print(exchange_rate_table.rates[1].currency)  # dolar amerykański

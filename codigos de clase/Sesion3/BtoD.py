from urllib.request import urlopen
import json

data = urlopen("http://api.bitcoincharts.com/v1/weighted_prices.json")

amount = float(input("Digite cantidad en BTC: "))
bitcoins = json.loads(data.read())
converted = float(bitcoins["USD"]["24h"]) * amount
print(f"$ {converted:.2f}")
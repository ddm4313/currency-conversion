import requests, json

base_currency = input("EUR/USD/NZD/CAD")
base_1 = float(input("Amount: "))
convert_tocurrency = input("EUR/NZD/USD/CAD")

rate = json.loads(requests.get(f"https://transferwise.com/gb/currency-converter/api/historic?source={base_currency}&target={convert_tocurrency}&period=30").text)[0]['rate']
print(f"Result: {float(base_1) * float(rate)}{convert_tocurrency}")

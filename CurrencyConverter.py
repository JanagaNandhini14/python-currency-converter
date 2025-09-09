import requests

def convert(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/latest?base={from_currency}&symbols={to_currency}"
    data = requests.get(url).json()

    if "rates" in data and to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        result = amount * rate
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("❌ Conversion failed. Response:", data)

# Example
convert(100, "USD", "INR")

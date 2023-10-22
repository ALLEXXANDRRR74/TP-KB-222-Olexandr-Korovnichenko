import requests

def convert(money, currency):
	try:
		url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
		response = requests.get(url)
		data = response.json()
		currency = data[0]["rate"]
	except Exception:
		print("Помилка отримання курсу")
		return "Невідомо"

	converted = money * currency
	return converted

currencys = ["EUR", "USD", "PLN"]

while True:
	currency = input("Введіть тип валюти (EUR, USD, PLN): ").upper()

	if currency == "Q":
		print("Закінчення роботи програми")
		break

	if currency in currencys:
		money = float(input(f"Введіть суму в {currency}: "))
		converted = convert(money, currency)
		print(f"{money} {currency} = {converted} UAH")
	else:
		print("Було введено невірний тип валюти")

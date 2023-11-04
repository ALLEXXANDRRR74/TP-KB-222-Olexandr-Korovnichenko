import logging

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def getA():
	while True:
		try:
			a = float(input("Введіть значення: "))
			logging.info(f"Введено значення a: {a}")
			return a
		except ValueError:
			print("Було введено невірне значення")

def getOp():
	while True:
		ops = ['+', '-', '*', '/', 'Q']
		op = input("Введіть операцію або 'Q' для виходу: ")
		if op in ops:
			logging.info(f"Введено операцію: {op}")
			return op
		else:
			print("Невідома операція")

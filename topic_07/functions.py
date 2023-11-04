import logging

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Functions:
	def getA(self):
		while True:
			try:
				a = float(input("Введіть значення: "))
				logging.info(f"Введено значення a: {a}")
				return a
			except ValueError:
				logging.error("Помилка невірного значення")
				print("Було введено невірне значення")

	def getOp(self):
		while True:
			ops = ['+', '-', '*', '/', 'Q']
			op = input("Введіть операцію або 'Q' для виходу: ")
			logging.info(f"Введено операцію: {op}")
			if op in ops:
				logging.info(f"Повернення операції")
				return op
			else:
				print("Невідома операція")

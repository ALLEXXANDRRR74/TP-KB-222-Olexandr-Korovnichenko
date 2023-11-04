import logging

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Operations:
	def CalcOperations(self, a, b, op):
		if op == "+":
			return a + b
		elif op == "-":
			return a - b
		elif op == "*":
			return a * b
		elif op == "/":
			try:
				return a / b
			except ZeroDivisionError:
				logging.error("Спроба ділення на нуль")
				return "Ділення на нуль"

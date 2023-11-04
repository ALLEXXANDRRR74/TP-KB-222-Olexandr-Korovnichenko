import logging
from functions import *
from operations import *

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

while True:
	logging.info("Отримання операції")
	op = getOp()

	if op == "Q":
		logging.info("Завершення роботи програми")
		break

	logging.info("Отримання значення А")
	a = getA()
	logging.info("Отримання значення Б")
	b = getA()

	if op == "+":
		result = plus(a, b)
	elif op == "-":
		result = minus(a, b)
	elif op == "*":
		result = multiplying(a, b)
	elif op == "/":
		result = division(a, b)

	logging.info(f"Введені дані: a = {a}, b = {b}, операція: {op}, результат: {result}")
	print(result)

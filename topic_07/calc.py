from functions import Functions
from operations import Operations
import logging

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

func = Functions()
ops = Operations()

while True:
	logging.info("Отримання операції")
	op = func.getOp()

	if op == "Q":
		print("Закінчення роботи програми")
		logging.info("Завершення роботи програми")
		break

	logging.info("Отримання значення А")
	a = func.getA()
	logging.info("Отримання значення Б")
	b = func.getA()

	result = ops.CalcOperations(a, b, op)
	logging.info(f"Введені дані: a = {a}, b = {b}, операція: {op}, результат: {result}")
	print(result)

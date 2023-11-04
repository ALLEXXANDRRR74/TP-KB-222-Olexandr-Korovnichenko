import logging

logging.basicConfig(filename='calclog.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def plus(a, b):
	result = a + b
	logging.info(f"Виконано додавання: {a} + {b} = {result}")
	return result

def minus(a, b):
	result = a - b
	logging.info(f"Виконано віднімання: {a} - {b} = {result}")
	return result

def multiplying(a, b):
	result = a * b
	logging.info(f"Виконано множення: {a} * {b} = {result}")
	return result

def division(a, b):
	try:
		result = a / b
		logging.info(f"Виконано ділення: {a} / {b} = {result}")
		return result
	except ZeroDivisionError:
		logging.error("Спроба ділення на нуль")
		return "Ділення на нуль"

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def multiplying(a, b):
	return a * b

def division(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return "Ділення на нуль"

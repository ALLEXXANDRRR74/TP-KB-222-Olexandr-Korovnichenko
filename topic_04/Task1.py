def getA():
	while True:
		try:
			a = float(input("Введіть значення: "))
			return a
		except ValueError:
			print("Було введено невірне значення")

def getOp():
	while True:
		ops = ['+', '-', '*', '/', 'Q']
		op = input("Введіть операцію або 'Q' для виходу: ")
		if op in ops:
			return op
		else:
			print("Невідома операція")


while True:
	op = getOp()

	if op == "Q":
		print("Закінчення роботи програми")
		break

	a = getA()
	b = getA()

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

	if op == "+":
		result = plus(a, b)
	elif op == "-":
		result = minus(a, b)
	elif op == "*":
		result = multiplying(a, b)
	elif op == "/":
		result = division(a, b)

	print(result)
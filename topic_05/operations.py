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

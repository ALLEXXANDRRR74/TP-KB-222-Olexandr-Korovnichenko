from functions import *
from operations import *

while True:
	op = getOp()

	if op == "Q":
		print("Закінчення роботи програми")
		break

	a = getA()
	b = getA()

	if op == "+":
		result = plus(a, b)
	elif op == "-":
		result = minus(a, b)
	elif op == "*":
		result = multiplying(a, b)
	elif op == "/":
		result = division(a, b)

	print(result)

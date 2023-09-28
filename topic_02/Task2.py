a = float(input("Перше значення: "))
b = float(input("Друге значення: "))
op = input("Операція: ")

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplying(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Ділення на нуль не можливе"
    else:
        return a / b

if op == "+":
    result = plus(a, b)
elif op == "-":
    result = minus(a, b)
elif op == "*":
    result = multiplying(a, b)
elif op == "/":
    result = division(a, b)
else:
    result = "Невідома операція"

print(result)
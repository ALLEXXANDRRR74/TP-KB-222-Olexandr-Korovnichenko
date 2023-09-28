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
        
match op:
    case "+":
        result = plus(a, b)
    case "-":
        result = minus(a, b)
    case "*":
        result = multiplying(a, b)
    case "/":
        result = division(a, b)
    case _:
        result = "Невідома операція"

print(result)
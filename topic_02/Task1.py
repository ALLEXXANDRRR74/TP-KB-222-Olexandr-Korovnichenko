a = -4
b = 2
c = 3

def discriminant(a:int, b:int, c:int):
    discriminant = b**2-4*a*c
    return(discriminant)

def root(a, b, c):
	discrim = discriminant(a, b, c)

	if discrim > 0:
		x1 = (-b+discrim**0.5)/(2*a)
		x2 = (-b-discrim**0.5)/(2*a)
		result = f"x1={x1}; x2={x2}"
		return result

	elif discrim == 0:
		x = -b / (2*a)
		result = f"x={x}"
		return result
	else:
		result = "Дискрімінант від'ємний"
		return result

print(root(a,b,c))
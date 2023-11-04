class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

StudentsList = [
	Student('Анна', 85),
	Student('Петро', 70),
	Student('Марія', 95),
	Student('Іван', 92),
	Student('Ірина', 85),
	Student('Андрій', 75),
	Student('Олександр', 100),
	Student('Наталія', 88)
]

result = sorted(StudentsList, key=lambda x: (x.age, x.name))

for student in result:
	print(f"Ім'я: {student.name}, Оцінка: {student.age}")

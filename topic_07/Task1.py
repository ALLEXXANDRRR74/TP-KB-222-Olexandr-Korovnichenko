class Person:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	def __str__(self):
		return f"Ім'я: {self.name}, Оцінка: {self.grade}"

	def __eq__(self, other):
		return self.name == other.name and self.grade == other.grade

	def __lt__(self, other):
		return self.grade < other.grade

student1 = Person("Василь", 82)
student2 = Person("Марія", 90)
student3 = Person("Олександр", 100)

print(student1)
print(student2)
print(student3)

print(student1 == student2)

print(student2 < student3)
from Student import StudentUnit

class CommandList:
	def __init__(self):
		self.students = []


	def printAllList(self):
		for student in self.students:
			text = f"Student name is {student.name}, Phone is {student.phone}, Age is {student.age}, Email is {student.email}"
			print(text)


	def addNewElement(self):
		name = input("Please enter student name: ")
		phone = input("Please enter student phone: ")
		age = int(input("Please enter student age: "))
		email = input("Please enter student email: ")

		student = StudentUnit(name, phone, age, email)
		self.students.append(student)
		self.students.sort(key=lambda x: (x.name, x.age))
		print("New element has been added")


	def deleteElement(self, name):
		deletePosition = -1
		for item in self.students:
			if name == item.name:
				deletePosition = self.students.index(item)
				break
		if deletePosition == -1:
			print("Element was not found")
		else:
			print(f"Delete position {str(deletePosition)}")
			del self.students[deletePosition]
		return


	def updateElement(self, name):
	    for index, student in enumerate(self.students):
	        if name == student.name:
	            print(f"Student {name} found")

	            new_name = input("Please enter new name: ")
	            if new_name and new_name != name:
	                del self.students[index]
	                new_student = StudentUnit(new_name, student.phone, student.age, student.email)
	                insert_position = 0
	                for item in self.students:
	                    if new_name > item.name:
	                        insert_position += 1
	                    else:
	                        break
	                self.students.insert(insert_position, new_student)

	            new_phone = input("Please enter updated phone: ")
	            if new_phone:
	                new_student.phone = new_phone

	            while True:
	                try:
	                    new_age = input("Please enter updated age: ")
	                    if new_age:
	                        new_student.age = int(new_age)
	                    break
	                except ValueError:
	                    print("Wrong student age")

	            new_email = input("Please enter updated email: ")
	            if new_email:
	                new_student.email = new_email

	            print("Element has been updated")
	            return

	    print("Student not found")


import csv
import sys

def printAllList():
	for elem in list:
		strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Age is {elem['age']}, Email is {elem['email']}"
		print(strForPrint)
	return


def addNewElement():
	name = input("Please enter student name: ")
	phone = input("Please enter student phone: ")
	age = int(input("Please enter student age: "))
	email = input("Please enter student email: ")
	
	newItem = {"name": name, "phone": phone, "age": age, "email": email}
	insertPosition = 0
	for item in list:
		if name > item["name"]:
			insertPosition += 1
		else:
			break
	list.insert(insertPosition, newItem)
	print("New element has been added")
	return


def deleteElement():
	name = input("Please enter name to be deleted: ")
	deletePosition = -1
	for item in list:
		if name == item["name"]:
			deletePosition = list.index(item)
			break
	if deletePosition == -1:
		print("Element was not found")
	else:
		print(f"Delete position {str(deletePosition)}")
		del list[deletePosition]
	return


def updateElement():
	name = input("Please enter name to be updated: ")
	for index, student in enumerate(list):
		if name == student["name"]:
			print(f"Student {name} found.")

			NewName = input("Please enter new name: ")

			if NewName and NewName != name:
				del list[index]
				student["name"] = NewName
				insertPosition = 0
				for item in list:
					if NewName > item["name"]:
						insertPosition += 1
					else:
						break
				list.insert(insertPosition, student)

			phone = input("Please enter new phone: ")
			age = input("Please enter new age: ")
			email = input("Please enter new email: ")

			student["phone"] = phone
			student["age"] = int(age)
			student["email"] = email    

			print("Element has been updated")
			return
	print("Student not found")


def LoadFile(file):
	with open(file, encoding="utf-8") as file:
		res = csv.DictReader(file)
		return [row for row in res]

def SaveFile(file, list):
	names = ["name", "phone", "age", "email"]
	try:
		with open(file, "w", newline="", encoding="utf-8") as file:
			result = csv.DictWriter(file, fieldnames=names)
			result.writeheader()
			result.writerows(list)
		print(f"The data is saved.")
	except IOError as e:
		print(f"Error saving")


list = [ ]

def main():
	if len(sys.argv) > 1:
		try:
			file = sys.argv[1]
			list.extend(LoadFile(file))
			print("Data loaded successfully.")
		except IOError as e:
			print("File upload error.")
	else:
		print("No CSV file specified.")
			
	while True:
		choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
		match choice.upper():
			case "C":
				print("New element will be created")
				addNewElement()
			case "U":
				print("Existing element will be updated")
				updateElement()
			case "D":
				print("Element will be deleted")
				deleteElement()
			case "P":
				print("List will be printed")
				printAllList()
			case "S":
				file = input("Enter a name for the CSV file: ")
				SaveFile(file, list)
			case "X":
				print("Exit")
				break
			case _:
				print("Wrong choice")


if __name__ == "__main__":
	main()
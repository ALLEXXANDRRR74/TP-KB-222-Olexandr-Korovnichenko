import sys
from Utils import FileUtils
from StudentList import CommandList

def main():
	Command_List = CommandList()
	Utils = FileUtils()

	if len(sys.argv) > 1:
		try:
			file = sys.argv[1]
			Utils.LoadFile(file, Command_List)
			print("Data loaded successfully.")
		except IOError as e:
			print("File upload error.")
	else:
		print("No CSV file specified.")

	while True:
		choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
		match choice.upper():
			case "C":
				print("New element will be created:")
				Command_List.addNewElement()
			case "U":
				print("Existing element will be updated")
				name = input("Please enter name to be updated: ")
				Command_List.updateElement(name)
			case "D":
				print("Element will be deleted")
				name = input("Please enter name to be deleted: ")
				Command_List.deleteElement(name)
			case "P":
				print("List will be printed")
				Command_List.printAllList()
			case "S":
				file = input("Enter a name for the CSV file: ")
				Utils.SaveFile(file, Command_List)
			case "X":
				print("Exit")
				break
			case _:
				print("Wrong choice")

if __name__ == "__main__":
	main()

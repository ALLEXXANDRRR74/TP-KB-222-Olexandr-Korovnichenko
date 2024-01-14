import csv
from Student import StudentUnit

class FileUtils:
	@staticmethod
	def LoadFile(file, Student_list):
		Student_list.students = []
		with open(file, encoding="utf-8") as file:
			result = csv.DictReader(file)
			Student_list.students.extend([StudentUnit(row["name"], row["phone"], row["age"], row["email"]) for row in result])
		return Student_list

	@staticmethod
	def SaveFile(file, Student_list):
		rows = ["name", "phone", "age", "email"]
		try:
			with open(file, "w", newline="", encoding="utf-8") as file:
				result = csv.DictWriter(file, fieldnames=rows)
				result.writeheader()
				result.writerows([vars(student) for student in Student_list.students])
			print(f"The data is saved")
		except IOError as e:
			print(f"Error saving")
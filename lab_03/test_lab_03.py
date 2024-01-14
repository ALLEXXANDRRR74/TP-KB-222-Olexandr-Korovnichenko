import pytest
from pathlib import Path
from io import StringIO
from unittest.mock import patch
from lab_03 import main
from Utils import FileUtils
from StudentList import CommandList
from Student import StudentUnit
import csv

@pytest.fixture
def TestingData():
	return [
		{"name": "Bob", "phone": "1112233", "age": "23", "email": "bob@example.com"},
		{"name": "Dilan", "phone": "2223344", "age": "18", "email": "Dilan@example.com"},
		{"name": "Zak", "phone": "3334455", "age": "20", "email": "zak@example.com"}
	]

def test_LoadFile(TestingData, tmp_path):
	PathFile = tmp_path / "lab3.csv"
	with open(PathFile, "w", newline="", encoding="utf-8") as file:
		ResFile = csv.DictWriter(file, fieldnames=["name", "phone", "age", "email"])
		ResFile.writeheader()
		ResFile.writerows(TestingData)

	LData = FileUtils.LoadFile(str(PathFile), CommandList())
	assert [vars(student) for student in LData.students] == TestingData

def test_SaveFile(TestingData, tmp_path, capsys):
	PathFile = tmp_path / "test_save_file.csv"
	StudentL = CommandList()
	StudentL.students = [StudentUnit(**data) for data in TestingData]

	FileUtils.SaveFile(str(PathFile), StudentL)

	captured = capsys.readouterr()
	assert "The data is saved\n" in captured.out

	LData = FileUtils.LoadFile(str(PathFile), CommandList())
	assert [vars(student) for student in LData.students] == [vars(student) for student in StudentL.students]

def test_updateElement(tmp_path, capsys, TestingData):
	with patch('builtins.input', side_effect=["John", "123", "30", "john@example.com"]):
		StudentL = CommandList()
		StudentL.students = [StudentUnit(**TestingData[0])]

		with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
			StudentL.updateElement("Bob")

		captured = TestInputAns.getvalue()
		assert "Element has been updated" in captured
		assert vars(StudentL.students[0]) == {"name": "John", "phone": "123", "age": 30, "email": "john@example.com"}
		assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students


def test_addNewElement(tmp_path, TestingData):
	StudentL = CommandList()

	with patch('builtins.input', side_effect=["Test", "123", "25", "test@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 1
	assert vars(StudentL.students[0]) == {"name": "Test", "phone": "123", "age": 25, "email": "test@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students

	with patch('builtins.input', side_effect=["AAA", "456", "30", "123@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 2
	assert vars(StudentL.students[0]) == {"name": "AAA", "phone": "456", "age": 30, "email": "123@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students

	with patch('builtins.input', side_effect=["Test", "222", "35", "test@example.com"]):
		StudentL.addNewElement()

	assert len(StudentL.students) == 3
	assert vars(StudentL.students[2]) == {"name": "Test", "phone": "222", "age": 35, "email": "test@example.com"}
	assert sorted(StudentL.students, key=lambda x: (x.name, x.age)) == StudentL.students


def test_deleteElement(capsys, TestingData):
	with patch('builtins.input', return_value="John"):
		StudentL = CommandList()
		StudentL.students = [StudentUnit(**TestingData[0])]

		with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
			StudentL.deleteElement("John")

		captured = TestInputAns.getvalue()
		assert "Element was not found\n" in captured

def test_printAllList(capsys, TestingData):
	StudentL = CommandList()
	StudentL.students = [StudentUnit(**TestingData[0])]

	with patch('sys.stdout', new_callable=StringIO) as TestInputAns:
		StudentL.printAllList()

	captured = TestInputAns.getvalue()
	assert "Student name is Bob, Phone is 1112233, Age is 23, Email is bob@example.com" in captured

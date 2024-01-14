import pytest
from lab_02 import LoadFile, SaveFile, addNewElement, deleteElement, updateElement, printAllList
from pathlib import Path
import csv
from io import StringIO

@pytest.fixture
def testing_data():
    return [
        {"name": "Bob", "phone": "1112233", "age": "20", "email": "bob@example.com"},
        {"name": "Dilan", "phone": "2223344", "age": "21", "email": "Dilan@example.com"},
        {"name": "Zak", "phone": "3334455", "age": "23", "email": "zak@example.com"}
    ]

def test_load_file(testing_data, tmp_path):
    path_file = tmp_path / "lab2.csv"
    with open(path_file, "w", newline="", encoding="utf-8") as file:
        result = csv.DictWriter(file, fieldnames=["name", "phone", "age", "email"])
        result.writeheader()
        result.writerows(testing_data)

    LoadedData = LoadFile(path_file)
    assert LoadedData == testing_data

def test_save_file(testing_data, tmp_path):
    path_file = tmp_path / "test_save_file.csv"
    SaveFile(path_file, testing_data)

    LoadedData = LoadFile(path_file)
    assert LoadedData == testing_data

def test_add_new_element(tmp_path, monkeypatch):
    lab_02_list = []

    test_input_ans = iter(["Test", "123", "25", "test@example.com"])

    def test_input(prompt):
        return next(test_input_ans)

    monkeypatch.setattr('builtins.input', test_input)
    monkeypatch.setattr('lab_02.list', lab_02_list)

    addNewElement()

    assert len(lab_02_list) == 1
    assert lab_02_list[0] == {"name": "Test", "phone": "123", "age": 25, "email": "test@example.com"}

def test_delete_element(capsys, monkeypatch):
    lab_02_list = [{"name": "John", "phone": "123", "age": 25, "email": "john@example.com"}]
    test_input_ans = iter(["John"])

    def test_input(prompt):
        return next(test_input_ans)

    monkeypatch.setattr('builtins.input', test_input)
    monkeypatch.setattr('lab_02.list', lab_02_list)

    deleteElement()

    captured = capsys.readouterr()
    assert "Del position" in captured.out

def test_update_element(tmp_path, capsys, monkeypatch):
    lab_02_list = [{"name": "John", "phone": "123", "age": "27", "email": "john@example.com"}]
    test_input_ans = iter(["John", "Jane", "123", "32", "john@example.com"])

    def test_input(prompt):
        return next(test_input_ans)

    monkeypatch.setattr('builtins.input', test_input)
    monkeypatch.setattr('lab_02.list', lab_02_list)

    updateElement()

    captured = capsys.readouterr()
    assert "Element has been updated" in captured.out
    assert lab_02_list[0] == {"name": "Jane", "phone": "123", "age": 32, "email": "john@example.com"}

def test_print_all_list(capsys, monkeypatch):
    lab_02_list = [{"name": "John", "phone": "123", "age": 25, "email": "john@example.com"}]
    monkeypatch.setattr('lab_02.list', lab_02_list)

    printAllList()

    captured = capsys.readouterr()
    assert "Student name is John, Phone is 123, Age is 25, Email is john@example.com" in captured.out

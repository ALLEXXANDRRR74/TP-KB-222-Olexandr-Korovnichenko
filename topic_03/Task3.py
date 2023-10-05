dicto = {"a": 1, "b": 2, "c": 3}

dicto.update({"d": 4, "e": 5})
print(f"Update: \n{dicto}")

del dicto["d"]
print(f"Del: \n{dicto}")

dicto.clear()
print(f"Clear: \n{dicto}")

dicto = {"a": 1, "b": 2, "c": 3}
print(f"Keys: \n{dicto.keys()}")

print(f"Values: \n{dicto.values()}")

print(f"Items: \n{dicto.items()}")


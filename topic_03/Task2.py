listo = [1, 2, 3, 4, 5]

listo.extend([6, 7, 8])
print(f"Extend: \n{listo}")

listo.append(10)
print(f"Append: \n{listo}")

listo.insert(2, 7)
print(f"Insert: \n{listo}")

listo.remove(3)
print(f"Remove: \n{listo}")

listo.clear()
print(f"Clear: \n{listo}")

listo = [10, 40, 20, 34, 1, 7]
listo.sort()
print(f"Sort: \n{listo}")

listo.reverse()
print(f"Reverse: \n{listo}")
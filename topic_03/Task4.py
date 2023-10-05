listo = ["а", "б", "д", "о"]

while True:
    text = input("Введіть значення для додання до списку або 'Q' для виходу: ")

    if text == 'Q':
        break

    index = 0

    for element in listo:
        if text > element:
            index += 1

    listo.insert(index, text)

    print(f"Список: {listo}")

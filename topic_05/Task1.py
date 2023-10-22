import random

while True:
	player_choice = input("Введіть камінь, ножиці або папір: ").lower()

	if player_choice == "q":
		print("Закінчення роботи програми")
		break

	choices = ["камінь", "ножиці", "папір"]
	pc_choice = random.choice(choices)

	print(f"Гравець: {player_choice}")
	print(f"Комп'ютер: {pc_choice}")

	if player_choice in choices:
		win = {
		    "камінь": "ножиці",
		    "ножиці": "папір",
		    "папір": "камінь"
		}

		if player_choice == pc_choice:
		    print("Нічия!")
		elif win[player_choice] == pc_choice:
		    print("Ви перемогли!")
		else:
		    print("Комп'ютер переміг!")
	else:
		print("Ви ввели неіснуючий жест")


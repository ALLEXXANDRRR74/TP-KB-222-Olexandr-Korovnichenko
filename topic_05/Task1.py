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
		if player_choice == pc_choice:
			print("Нічия!")
		elif (player_choice == "камінь" and pc_choice == "ножиці") or \
			 (player_choice == "ножиці" and pc_choice == "папір") or \
			 (player_choice == "папір" and pc_choice == "камінь"):
			print("Перемога гравця")
		else:
			print("Перемога Комп'ютера")
	else:
		print("Ви ввели неіснуючий жест")


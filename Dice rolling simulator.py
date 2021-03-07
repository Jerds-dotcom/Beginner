import random

while True:
	user_input = input('Press enter to roll or type "x" to stop: ')

	if user_input.lower().strip() == 'x':
		break

	roll = random.randint(1, 6)
	print(roll)

print('Thanks for playing')
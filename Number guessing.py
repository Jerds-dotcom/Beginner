import random

score = 5
ran_num = random.randint(1, 100)

if ran_num <= 50:
	print('Random number is less than 51')
elif ran_num > 50:
	print('Random number is greaten than 50')

while True:
	try:
		guess = int(input('Enter a number between 1 to 10: '))

		if guess == ran_num:
			print(f'You got it! \nScore: {score}')
			break

		elif guess != ran_num:
			score -= 1

		if score == 0:
			print('You lose!')
			break
	except:
		print('Invalid input try again.')
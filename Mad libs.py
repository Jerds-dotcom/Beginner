
def words_from_user(words):
	user_words = []
	for word in words:
		user_input = input(word + ': ')
		user_words.append(user_input)

	return user_words

words = words_from_user(['Noun', 'Verb', 'Adjective'])

temp = f'I have a big {words[0]}, I like to {words[1]} and I am very {words[-1]}'
print(temp)
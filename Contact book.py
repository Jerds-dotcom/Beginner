
requirements = ['Name', 'Address', 'Phone number', 'Email']

def Contact_info(data):
	user_data = []
	for i in data:
		user_input = input(i + ': ')
		user_data.append(user_input)
	while not user_data[2].isdigit():
		user_data.pop(2)
		print('Phone number must be your contact information')
		user_input = input(data[2] + ': ')
		user_data.insert(2, user_input)
	return user_data

data = Contact_info(requirements)

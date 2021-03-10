from plyer import notification

title = 'Take a break'
message = 'You need to rest'

def notify_me(title, message):
	notification.notify(
		title = title,
		message = message,
		app_icon = "C:\\Users\\Jerds\\Downloads\\pic.ico",
		timeout = 10
	)

if __name__ == '__main__':
	notify_me(title, message)
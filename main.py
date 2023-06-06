

def main():
	import prints
	prints.startAscii()

	prints.menu()
	choice = input("Enter your choice: ")
	
	import handler
	for i in range(1, handler.Choices().TotalChoices + 1):
		"""
		Checks if the user's choice is valid.
		"""
		if choice == str(i):
			choice = "c" + choice
			choice = getattr(handler.Choices(), choice)()
			break
		else:
			pass

main() # Not using an if statement because I want to be able to call this function from other files.

# Path: main.py
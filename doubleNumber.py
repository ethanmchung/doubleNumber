userNumber = input("Tell me a number. ")

x = 4

while x == 4:
	try:
		userNumber = int(userNumber)
		#only put lines that you expect to cause exceptions here
		x = 3
	except ValueError:
		print("That's not a number you idiot")
		userNumber = input("Tell me a number. ")
print("Double that is {}.".format(userNumber * 2))
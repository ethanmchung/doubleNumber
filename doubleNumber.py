userNumber = input("Tell me a number. ")

x = 3
while x != 4:
	try:
		userNumber = int(userNumber)
		x = 4
		#only put lines that you expect to cause exceptions here
	except ValueError:
		print("That's not a number you idiot")
		userNumber = input("Tell me a number. ")
print("Double that is {}.".format(userNumber * 2))
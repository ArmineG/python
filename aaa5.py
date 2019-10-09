def tuple1():
	user_name = input("Enter your name")
	user_surname = input("Enter your surname")
	return user_name, user_surname
user_info = tuple1()

print("Your name is " + user_info[0])
print("Your surname is " + user_info [1])
try:
	input_file = open("Numberfile.txt", mode = "r")
	try:
		for line in input_file:
			print(int(line))
	except ValueError:
		print("A value error occured")
	else: 
		print("No errors ocurred")
	finally:
		input_file.close()
except: I0Error:
	print("An Error occured reading the file!")

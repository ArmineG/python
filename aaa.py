my_string = "This string is not a number"
try:
	print("Converting my_string to int...")
	1/0
	print("String #" + 1 + ":" + my_string)
	my_int = int (my_string)
	print (my_int)
except ValueError:
	print("Can't convert; my_strong to a number")
except TypeError:
	print("Can't concatinate number with string")
except: 
	print("Unknown error")
print ("Done!")
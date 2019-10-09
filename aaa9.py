def averege(in_list):
	sum=0
	for number in in_list:
		sum+=number
	return sum/ len(in_list)
my_list1 = [1, 2,3,4,5,6,7]
my_list2 = [91,92,93,94,95,96,97]
print("The avarage of my_list1 is:", averege(my_list1))
print("The avarage of my_list2 is:", averege(my_list2))
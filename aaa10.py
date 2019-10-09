def two_D_average(in_2d_list):
	result = []
	for num_list in in_2d_list:
		sum = 0 
		for number in num_list:
			sum+=number
		result.append(sum/len(num_list))
	return result

my_2d_list = [[61, 32, 12, 123], [123, 131, 131, 123], [4, 1, 2]]
print("average:", two_D_average(my_2d_list))

def get_middle_three_chars (sample_str):
	middle_index = int (len(sample_str)/2)
	print("Original String is", sample_str)
	middle_three = sample_str[middle_index-1: middle_index+2]
	print("Middle three chars are", middle_three)
print(get_middle_three_chars("JhonDipPeta"))
print(get_middle_three_chars("Jasonay"))


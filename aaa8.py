my_list = [1, 2, 3, 4 ]
my_list.append(5)
print(my_list, ": After appening five")
new_list = [6, 7, 8]
my_list.extend(new_list)
print(my_list, ": After extending")
my_list.insert(0, 0)
print(my_list, ': After inserting zero')
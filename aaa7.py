my_list = [0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
my_list.remove(23)
print(my_list, ': After removing 23')
my_list.sort()
print(my_list, ': After sorting')
my_list.reverse()
print(my_list, ':After reversing')
my_list.pop()
print(my_list, ": poping")

del my_list[-5:]
print(my_list, ": After deleting the last five items")
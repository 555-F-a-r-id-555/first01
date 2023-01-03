my_list_1 = [2, 5, 5, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list = list()
for i, x in enumerate(my_list_1):
    if x not in my_list_2:
        my_list.append(x)
print(my_list)

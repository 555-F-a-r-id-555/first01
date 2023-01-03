my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list = list()
for x in my_list_1:
    if my_list_1.count(x) == 1:
        my_list.append(x)
print(my_list)


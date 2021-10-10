num_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [x for x in num_list if num_list.count(x) == 1]
print(result)
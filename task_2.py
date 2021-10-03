eg_list = input('List ')
input_list = eg_list.split()
len_list = len(input_list)
i = 0
while i < len_list-1:
    a = input_list[i]
    input_list[i] = input_list[i+1]
    input_list[i+1] = a
    i += 2

print(input_list)
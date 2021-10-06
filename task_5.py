def sum_nums(str_num, stop):
    list_nums = str_num.split(' ')
    sum_list = 0
    for i in list_nums:
        if i == stop:
            break
        sum_list += int(i)

    return sum_list

stopper = '$'
finished = False
s = 0
while not finished:
    user_num_str = input('вводите числа разделенные пробелом: ')
    s += sum_nums(user_num_str, stopper)
    finished = stopper in user_num_str
    print(f'sum = {s}')





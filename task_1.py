
def div_num(num_1, num_2):
    if num_2 == 0:
        return "You can not divine to zero!"
    else:
         return num_1 / num_2

num_1 = int(input('введите делимое: '))
num_2 = int(input('введите делитель: '))

print(div_num (num_1, num_2))
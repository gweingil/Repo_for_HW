def my_func (x, y):
    if x < 0:
        return "x must be greater than 0"
    if y > 0:
        return "y must be less than 0"
    r = 1
    for i in range(y*-1):
        r *= x
    return 1 / r

x = int(input('введите положительное число: '))
y = int(input('введите отрицательное число: '))

print(my_func(x, y))

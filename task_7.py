def fact(number):
    cur = 1
    for i in range (1, number + 1):
        cur *= i
        yield cur

n = 12
for ind, el in enumerate(fact(n)):
    print(f'#{ind +1} {el}')

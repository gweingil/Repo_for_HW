with open ('new_test.txt', 'w') as file:
    input_line = input('Введите текст: \n')
    while input_line:
        file.write(f'{input_line} \n' )
        input_line = input('Введите текст: \n')
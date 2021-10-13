with open('new_test_1.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_inf = file_lines.slit()
        employees.update({emp_inf[0]: float(emp_inf[1])})
        sum_salary += float(emp_inf[1])
average_salary = sum_salary / len(employees)
print(f'Average: {average_salary}')

for a, b in employees.items():
    if b < 20000:
        print(f'{a}: {b}')
def user_inf(name, surname,year_of_birth, city, email, phone):
    print (f'{name}, {surname},{year_of_birth}, {city}, {email}, {phone}')

n = input('Name ')
s = input('Surname ')
y = input('Year_of_birth ')
c = input('City ')
e = input('Email ')
p = input('Phone ')

user_inf(name=n, surname=s, year_of_birth=y, city=c, email=e, phone=p)


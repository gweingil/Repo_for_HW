class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong months'
        else:
            return f'Wrong day'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('23 - 10 - 2021')
print(today)
print(Data.valid(23, 12, 2019))
print(today.valid(23, 13, 2010))
print(Data.extract('23 - 09 - 2022'))
print(today.extract('23 - 03 - 2019'))
print(Data.valid(10, 23, 2003))

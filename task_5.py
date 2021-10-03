rating_list = [10, 9, 8, 7, 6, 5, 4]

rating = int(input('введите новый элемент рейтинга' ))
inserted = False
for index, elem in enumerate(rating_list):
    if rating > elem:
        rating_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    rating_list.append(rating)

print(rating_list)

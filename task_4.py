user_sentence = input('Введите предложение ')

word = user_sentence.split()

for num, word in enumerate(word):
    print(f'#{num} {word:10}')
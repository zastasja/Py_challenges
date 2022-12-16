# Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.
word = input().lower()
letters = []
count = 0

for i in word:
    if i in letters:
        count += 1
    letters.append(i)
print(count)
print(letters)

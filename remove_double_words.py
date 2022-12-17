# Удаляем слова-дубли
# В качестве ответа необходимо вывести итоговую строку без дублей без изменения регистра

s = input().split()

sorted_list = []
result = []

for i in range(len(s)):
    if s[i].lower() not in sorted_list:
        sorted_list.append(s[i].lower())
        result.append(s[i])

print(*result)

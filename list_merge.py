
# слияние отсортированных списков
n, m = int('Введите количество чисел', input()), int('Введите количество чисел', input())
list1 = list(map(int,'Введите отсортированные числа по возрастанию через пробел', input().split()))
list2 = list(map(int,'Введите отсортированные числа по возрастанию через пробел', input().split()))
i, j = 0, 0
res = []
while i < n and j < m:
    if list1[i] < list2[j]:
        res.append(list1[i])
        i += 1
    else:
        res.append(list2[j])
        j += 1
while i < n:
    res.append(list1[i])
    i += 1
while j < m:
    res.append(list2[j])
    j += 1

print(*res)


# слияние отсортированных списков
n, m = map(int,'Введите количество чисел через пробел', input().split()))
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
if i < n:
    res = res + list1[i:]
if j < m:
    res = res + list2[j:]

print(*res)

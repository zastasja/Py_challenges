# bubble sort
n = int('Введите количество чисел', input())
nums = list(map(int,'Введите числа для сортировки через пробел', input().split()))
count = 0
for run in range(n - 1):
    for i in range(n - 1 - run):
        if nums[i] > nums[i + 1]:
            count += 1
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(*nums)
print(count)


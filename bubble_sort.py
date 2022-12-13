# bubble sort
n = 6
nums = [5, 7, 4, 3, 8, 2]
count = 0
for run in range(n - 1):
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(*nums)
print(count)

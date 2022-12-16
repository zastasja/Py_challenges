# посчитать цифры в строке и их сумму
s = input()
count = 0
nums = []
for i in s:
    if i.isdigit():
        count += 1
        nums.append(i)

sum_digits = 0
for x in nums:
    n = int(x)
    sum_digits += n
print(count, sum_digits)

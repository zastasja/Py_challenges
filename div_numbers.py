#Какова сумма всех натуральных делителей числа 34?
from functools import reduce

n = int(input())
i = 1
d = []

while i**2 <= n:
    if n%i == 0:
        d.append(i)
        if i != n:
            d.append(n//i)
    i+=1
d.sort()

print(reduce(lambda x,y: x+y, d))

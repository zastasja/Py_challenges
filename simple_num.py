# Дано натуральное число N. Определить, является ли оно простым. 
# Натуральное число N называется простым, если у него есть только два делителя: единица и само число N. 
# В качестве ответа выведите "Yes", если число простое,  "No" - в противном случае.


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

if 1 < len(d) <= 2:
    print('Yes')
else:
    print('No')



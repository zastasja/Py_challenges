#сортировка c подсчетом

#Example 1
a = [2, 3, 4, 1, 2, 2, 4, 5]
count = [0] * 6

for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')
print()

#Example 2

s = "asdfg DFGH 1234 ghjk SDF ;$%ˆ&"
letters = [0] * 26
for i in s.lower():
    if i >= 'a' and i <= 'z':
        number = ord(i) - 97
        letters[number] += 1

for i in range(26):
    if letters[i] > 0:
        # print(chr(i + 97), letters[i])
        print(chr(i+97)*letters[i], end='')
print()

#Example 3

import random
a=[]
for i in range(10):
    a.append(random.randint(-10,10))

count = [0]*21
for i in a:
    count[i+10] +=1

for i in range(21):
    print(i-10, count[i])

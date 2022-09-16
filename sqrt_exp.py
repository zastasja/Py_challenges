#Квадратное уравнение
#ax**2+bx+c=0

import math
a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    maxi = max(x1, x2)
    mini = min(x1, x2)
    print(mini, maxi, sep="\n")

elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')
    

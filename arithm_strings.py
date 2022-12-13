# Арифметические строки
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

a, b, c = input(), input(), input()
mini = min(len(a), len(b), len(c))
maxi = max(len(a), len(b), len(c))

if (mini+maxi)/2 == (len(a)+len(b)+len(c))/3:
    print('YES')
else:
    print('NO')

#Первая цифра после точки
#Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

a = float(input())
b = int(a)
c = a-b
d = c*10
res = int(d)
print(res)
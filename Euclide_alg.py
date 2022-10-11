# Алгоритм Эвклида
# Алгоритм Евклида позволяет найти наибольший общий делитель (НОД) для двух чисел
# Variant 1

a, b = int(input()), int(input())

while a != b:
  if a>b:
    a=a-b
  elif a<b:
    b=b-a
print(a)

#####
# Variant 2
a, b = int(input()), int(input())

while b > 0:
  c = a % b
  a = b
  b = c

print(a)
  

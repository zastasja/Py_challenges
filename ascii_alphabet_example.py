# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...].
from string import ascii_uppercase

n = int(input())
alfabet = list(ascii_uppercase)
l = [alfabet[i] for i in range(n) ]
print(l)

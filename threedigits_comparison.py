# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.

a, b, c = int(input()), int(input()), int(input())
maxi = max(a,b,c)
mini = min(a,b,c)
midi = (a+b+c)-(mini+maxi)
print(maxi, midi, mini, sep="\n")
#Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city1, city2, city3 = input(), input(),input()

mini = min(city1, city2, city3, key=len)
maxi = max(city1, city2, city3, key=len)
print(mini, maxi, sep="\n")

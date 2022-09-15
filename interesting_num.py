#Интересное число
#Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
num = int(input())
first = num//100
third = num%10
second = (num%100 - third)//10
mini = min(third, second, first)
maxi = max(third, second, first)
midi = (first+second+third)-(maxi+mini)
diff = maxi - mini

if diff == midi:
    print("Число интересное")
else:
    print("Число неинтересное")

#Напишите программу, вычисляющую значение тригонометрического выражения
import math

degree = float(input())
r = math.radians(degree)
trig = math.sin(r)+math.cos(r)+math.tan(r)**2
print(trig)

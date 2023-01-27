# Условия задачи.
# Строительная компания построила небоскреб, в котором floors этажей, и хочет посчитать, какую выручку она сможет получить от продажи всех квартир.

# На каждом этаже находится только одна квартира. Стоимость квартиры зависит от того, на каком этаже она находится.
# Стоимость квартиры возрастает на 1000 долларов каждые increase этажей. Стоимость квартиры на первом этаже составляет main_price долларов.
# Вам даны целые положительные числа floors, increase, main_price.

floors, increase, main_price = int(input()),int(input()),int(input())
extra_pay = 1000
res = 0

for i in range(floors):
  if i < increase:
    res += main_price
  elif i >= increase:
    res += main_price+extra_pay*(i//increase)
 
print(f"Итого стоимость за дом: {res}")

# floors, increase, main_price = 30, 10, 10000
# assert res == 330000

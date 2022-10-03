#While loops with digits:
n = int(input('Введите целочисленное число: '))
count = 0
count_even = 0
sum_num = 0
mult_num = 1
maxi_num = 0
mini_num = 9
while n > 0:
    last = n % 10
    count += 1
    if last % 2 == 0:
        count_even +=1
    sum_num = sum_num + last
    mult_num = mult_num * last
    if last > maxi_num:
        maxi_num = last
    if last < mini_num:
        mini_num = last
    n = n // 10

print(f'Всего цифр {count}')
print(f'Всего четных цифр {count_even}')
print(f'Сумма всех чисел {sum_num}')
print(f'Произведение всех чисел {mult_num}')
print(f'Максимальное число {maxi_num}')
print(f'Минимальное число {mini_num}')

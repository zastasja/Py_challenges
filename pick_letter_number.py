# Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'

#сумма чисел из списка
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
my_num = ([x for x in list_1 if isinstance(x, (int, float))])
print(sum(my_num))

#слова содержащие только букву 'a' из списка
my_word = ([y for y in list_1 if isinstance(y, str)])
new_list = [z for z in my_word if 'a' in z]
print(new_list)

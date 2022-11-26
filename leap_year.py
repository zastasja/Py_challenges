year = int(input())

if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

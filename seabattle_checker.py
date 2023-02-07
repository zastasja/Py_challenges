def seabattle_ships():
    one = 0
    two = 0
    three = 0
    four = 0
    num = int(input())
    for i in range(num):
        ships = map(int, input().split())
        print(ships)
        for i in ships:
            if i == 1:
                one += 1
            elif i == 2:
                two += 1
            elif i == 3:
                three += 1
            elif i == 4:
                four += 1

    if one == 4 and two == 3 and three == 2 and four == 1:
        print('YES')
    else:
        print('NO')

seabattle_ships()

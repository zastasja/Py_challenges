# match practice

znak = input()
match znak:
    case 'Овен' | 'Лев' | 'Стрелец':
        print('Огненный')
    case 'Телец' | 'Дева' | 'Козерог':
        print('Земной')
    case 'Близнецы' | 'Весы' | 'Водолей':
        print('Воздушный')
    case 'Рак' | 'Скорпион' | 'Рыбы':
        print('Водный')



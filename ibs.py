separator = '\n' + '=' * 100

# Сгенерировать список от 0 до 100 отсортированный на убывание, где числа нечётные и кратны 3
print('Сгенерировать список от 0 до 100 отсортированный на убывание, где числа нечётные и кратны 3')
result: list = None
l = []
for i in range(101):
    if i % 2 != 0 and i % 3 == 0:
        l.append(i)

result = sorted(l, reverse=True)
print(f'Результат: {result}\n')
assert (
    result == [99, 93, 87, 81, 75, 69, 63, 57, 51, 45, 39, 33, 27, 21, 15, 9, 3],
    'Не удалось сгенерировать список!'
)

print(separator)
# Объединить два списка в один (желательно несколько способов)
print('Объединить два списка в один (желательно несколько способов)')
a = [1, 2, 3]
b = [3, 4, 5]

result_1: list = a+b
result_2: list = [x for x in a+b]

print(f'Результат 1-ый : {result_1}')
print(f'Результат 2-ой : {result_2}\n')
assert (
    all(map(lambda x: x == [1, 2, 3, 3, 4, 5], [result_1, result_2])),
    'Не пройдена проверка с объединением списков!')

print(separator)
# Сбросить дубликаты из списка
print('Сбросить дубликаты из списка')

c = [1, 1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
result: list = list(set(c))

print(f'Результат: {result}\n')
assert result == [1, 2, 3, 4, 5, 6, 7], 'не удалось корректно убрать дубликаты'


print(separator)
# Написать класс Vector с двумя полями x и y типа инт
# Реализовать возможность сложения двух объектов класса Vector через оператор сложения "+" | x1 + x2 ; y1 + y2
# В результате сложения получается новый объект класса Vector
print("Написать класс Vector с реализацией сложения объектов")


class Vector:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

# Раскомментировать при решении задачи
v1 = Vector(x=1, y=1)
v2 = Vector(x=4, y=-5)
v3 = v1 + v2

print(f'\nРезультирующий вектор: x={v3.x}, y={v3.y}\n')
assert v3.x == 5
assert v3.y == -4


print(separator)
# Написать абстрактный класс "Figure", в котором содержится пустой метод calc_area()
# Написать классы "Square", "Circle", которые наследуются и переопределяют метод calc_area() для каждой фигуры
# Класс "Square" имеет поле side (сторона) типа int
# Класс "Circle" имеет поле radius (радиус) типа int
print('Написать абстракцию, и классы которые наследуются и переопределяют метод')
from math import pi


class Figure:
    def calc_area(self):
        pass


class Square(Figure):
    def __init__(self, side: int):
        self.side = side

    def calc_area(self, side):
        return self.side * self.side

class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    def calc_area(self, radius):
        return math.pi * self.radius * self.radius

# Раскомментировать при решении задачи
square = Square(side=4)
circle = Circle(radius=3)

print(f'Площадь Квадрата={square.calc_area()}\nПлощадь Круга={circle.calc_area()}')
assert square.calc_area() == 16, 'Неверно посчитана площадь квадрата!'
assert circle.calc_area() == 28.274333882308138, 'Неверно посчитана площадь круга!'


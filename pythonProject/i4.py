import numpy

a = numpy.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
b = numpy.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
c = a + b
c1 = a - b
c2 = a * b
c3 = a / b
c4 = a ** b
print('Сложение')
print(c)
print('Вычитание')
print(c1)
print('Умножение')
print(c2)
print('Деление')
print(c3)
print('Возведение в степень')
print(c4)
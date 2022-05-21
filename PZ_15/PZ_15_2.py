# В матрице элементы третьей строки заменить элементами из одномерного динамического массива соответствующей размерности.


import random
n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]
print('Начальная матрица: ')
for i in matrix:
    print(*i)

t = n
a = [0] * t
for i in range(t):
    a[i] = int(input('Введите элементы одномерного массива: '))

print('Ваш одномерный массив: ')
for i in a:
    print(i, end='')
print('\n')

for i in range(m):
    matrix[2][i] = a[i]

print('Полученная матрица: ')
for i in matrix:
    print(*i)
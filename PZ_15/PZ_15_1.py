# В матрице элементы последнего столбца заменить на -1.


import random
n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]

print('Начальная матрица: ')
for i in matrix:
    print(*i)
    
for i in range(m):
    matrix[i][n-1] = -1

print('Полученная матрица: ')
for i in matrix:
    print(*i)


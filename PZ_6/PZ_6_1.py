# Пользователь вводит размер списка А, элементы выдаются рандомно.
# Программа выдает рандомно число К от 1 до N(это и есть размер списка).
# Нумерация элементов списка начинается с 0.
# Далее каждый элемент списка увеличивается на число под номером К и выводится на экран новый список А.


import random
A = []
for N in range(int(input('Введите размер списка: '))):
    A.append(random.randint(0,100))
print('Список: ',A)


K = random.randrange(0,N)
print('Элемент под номером: ',K,', учитывая, что нумерация начинается с 0')
print('A[{0}] = {1}'.format(K,A[K]))

x = A[K]
A = [N + x for N in A]
print('Новые значения списка A: ',A)


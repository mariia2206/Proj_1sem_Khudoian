A = input('Введите целое положительное число A: ')
B = input('Введите целое положительное число B: ')
C = input('Введите целое положительное число C: ')

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Неправильно ввели')
        A = input('Введите целое число A: ')
    if int(A) <= 0:
        print('Неправильно ввели')
        A = input('Введите целое положительное  число A: ')

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Неправильно ввели')
        B = input('Введите целое число B: ')
    if int(B) <= 0:
        print('Неправильно ввели')
        B = input('Введите целое положительное  число B: ')

while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print('Неправильно ввели')
        C = input('Введите целое число C: ')
    if int(C) <= 0:
        print('Неправильно ввели')
        C = input('Введите целое положительное  число C: ')
k = 0
while A - C >= 0:
    A -= C
    B2 = B
    while B2 - C >= 0:
        B2 -= C
        k +=1
print ('Количество квадратов: ' ,k)

# Дано целое положительное число N.
# Найти произведение 1.1 * 1.2 * 1.3 * ...(N сомножителей).
# Делаем проверку исключений.

proizv = 1
k = 1
N = input('Введите целое положительное число N: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели')
        N = input('Введите целое число N: ')
    if int(N) <= 0:
        print('Неправильно ввели')
        N = input('Введите целое положительное  число N: ')

while k <= N:
    k += 0.1
    proizv *= k

print('Произведение = ', proizv)




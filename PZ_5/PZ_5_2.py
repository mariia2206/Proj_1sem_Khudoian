# Дано 4 переменных, которые должен ввести пользователь A,B,C,D.
# Нужно описать функцию swap(x,y) меняющую содержимое переменных x и y.
# x и y - вещественные параметры, являющиеся одновременно входными и выходными.
# С ее помощью для A,B,C,D последовательно поменять содержимое следующих пар: A и B, C и D, B и C.
# Вывести новые значения A,B,C,D.

def swap(x, y):
    x, y = y, x
    return x, y


a = float(input('Ввести данные для переменной A: '))
b = float(input('Ввести данные для переменной B: '))
c = float(input('Ввести данные для переменной C: '))
d = float(input('Ввести данные для переменной D: '))

a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)

print('Новые зачения A,B,C,D: ', a, b, c, d)
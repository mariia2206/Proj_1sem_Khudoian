# Пользователь вводит строку, содержащую хотя бы 1 символ пробела.
# Программа выводит подстроку, расположенную между первым и вторым пробелом исходной строки.
# Если строка содержит только один пробел, то выводит пустую строку.


stroka = input('Введите строку, содержащую хотя бы 1 пробел: ')
a = stroka.count(' ') > 1
result = a * stroka.split()[1]
print('Подстрока: ', result)

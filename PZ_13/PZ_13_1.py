# Организовать и вывести последовательность на N произвольных целых элементов.
# Cформировать новую последовательность куда поместить положительные четные элементы.
# Найти их сумму и среднее арифметическое.


from random import randint
n = [randint(-9, 9) for i in range(int(input('Введите количество элементов:')))]
print(n)

d = [i for i in n if i > 0 if i % 2 == 0]
print('Положительные четные элементы:',d,'\n''Их сумма:', str(sum(d)), '\n''Среднее арифметическое:', str(sum(d) / len(d)))
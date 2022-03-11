# Составить генератор (yield), который преобразует все буквенные символы в строчные.


def lower_letters(n):
    yield from [i.lower() for i in n]

print('Введите буквенные символы:')
print('Строчные символы: ',''.join([o for o in lower_letters(input())]))

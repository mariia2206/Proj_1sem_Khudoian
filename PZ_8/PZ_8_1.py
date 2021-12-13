# Дан словарь d = {'a':1, 'b':2,'c':3}.
# Выполнить сортировку словаря по убыванию.


d = {'a':1, 'b':2,'c':3}
print('Начальный словарь:', d)

a = sorted(d, reverse=True)
b = sorted(d.values(), reverse=True)
print('Отсортированный по убыванию словарь: ')
print(dict(zip(a,b)))
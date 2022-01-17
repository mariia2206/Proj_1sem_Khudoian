# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев.
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах нельзя приобрести книги Грибоедова или Маяковского.


magistr = {'Лермонтов', 'Достоевский','Пушкин','Тютчев'}
domkhigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bookmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galery = {'Чехов', 'Тютчев', 'Пушкин'}
pic = {'Грибоедов', 'Маяковский'}
a = {'Грибоедов'}
b = {'Маяковский'}

if magistr & pic == set():
    print('Книги Маяковского и Грибоедова нельзя приобрести в Магистре')
elif magistr & a == set():
    print('Книги Грибоедова нельзя приобрести Магистре')
elif magistr & b == set():
    print('Книги Маяковского нельзя приобрести Магистре')

if domkhigi & pic == set():
    print('Книги Маяковского и Грибоедова нельзя приобрести в ДомеКниги')
elif domkhigi & a == set():
    print('Книги Грибоедова нельзя приобрести в ДомеКниги')
elif domkhigi & b == set():
    print('Книги Маяковского нельзя приобрести ДомеКниги')

if bookmarket & pic == set():
    print('Книги Маяковского и Грибоедова нельзя приобрести в БукМаркете')
elif bookmarket & a == set():
    print('Книги Грибоедова нельзя приобрести в БукМаркете')
elif bookmarket & b == set():
    print('Книги Маяковского нельзя приобрести в БукМаркете')

if galery & pic == set():
    print('Книги Маяковского и Грибоедова нельзя приобрести в Галерее')
elif galery & a == set():
    print('Книги Грибоедова нельзя приобрести в Галерее')
elif galery & b == set():
    print('Книги Маяковского нельзя приобрести в Галерее')
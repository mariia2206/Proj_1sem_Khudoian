# Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Количество элементов, общих для двух файлов:
# Количество четных элементов первого файла:
# Количество нечетных элементов второго файла:


l = ['2 45 6 90 89 3']
f1 = open('data_1.txt', 'w',encoding='utf-8')
f1.writelines(l)
f1.close()

m = ['-2 -6 -56 -90 -5 -7']
f2 = open('data_2.txt', 'w',encoding='utf-8')
f2.writelines(m)
f2.close()

f3 = open('data_3.txt', 'w',encoding='utf-8')
f3.write('Элементы первого и второго файлов: ')
f3.write('\n')
f3.writelines(l)
f3.writelines(m)
f3.write('\n')
f3.close()

f3 = open('data_3.txt', 'a',encoding='utf-8')
f3.write('Количество элементов первого и второго файлов: ')
f3.write('\n')
f3.close

f1 = open('data_1.txt',encoding='utf-8')
k = f1.read()
k = k.split()
f1.close()
f2 = open('data_2.txt',encoding='utf-8')
g = f2.read()
g = g.split()
o = len(k)+len(g)
f2.close

f3 = open('data_3.txt', 'a',encoding='utf-8')
f3.writelines(str(o))
f3.close()

f3 = open('data_3.txt', 'a',encoding='utf-8')
f3.write('\n')
f3.writelines('Количество элементов общих для двух файлов:')
c = []
for i in k:
    for j in g:
        if i == j:
            c.append(i)
            break

if c == []:
    c = 0
    print(c)
else:
    print(c)
f3.write('\n')
f3.write(str(c))
f3.write('\n')
f3.close

f3 = open('data_3.txt', 'a',encoding='utf-8')
f3.writelines('Количество четных элементов первого файла:')

count = 0
for x in k:
    if int(x) % 2 == 0:
        count += 1
print(count)
f3.write('\n')
f3.write(str(count))
f3.write('\n')
f3.close

f3 = open('data_3.txt', 'a',encoding='utf-8')
f3.writelines('Количество нечетных элементов второго файла:')

count = 0
for x in g:
    if int(x) % 2 == 1:
        count += 1
print(count)
f3.write('\n')
f3.write(str(count))
f3.close()











# Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое, количество символов в тексте.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей.


file = open('text18-29.txt', encoding ='UTF-8')
print('Содержимое файла: ')
print(file.read())

print('Количество символов в тексте: ')
file = open('text18-29.txt','r', encoding ='UTF-8').read()
print(len(file))

file = open('text18-29.txt', encoding ='UTF-8')
l = file.readlines()
l[5],l[6] = l[6],l[5]
l[4], l[5] = l[5], l[4]
l[3], l[4] = l[4], l[3]
l[2], l[3] = l[3],l[2]
file.close
f2 = open('text18-2.txt', 'w')
f2.writelines(l)
f2.close

print(open('text18-29.txt').read(), '\n' + str(len(open('text18-29.txt').read())))
print(open('text18-29.txt').read().splitlines()[0], '\n' + str(open('text18-29.txt').read().splitlines()[1]), '\n' +
      str(open('text18-29.txt').read().splitlines()[-1]), '\n' + str(open('text18-29.txt').read().splitlines()[2]), '\n' +
      str(open('text18-29.txt').read().splitlines()[3]), '\n' + str(open('text18-29.txt').read().splitlines()[4]), '\n' +
      str(open('text18-29.txt').read().splitlines()[5]), file=open('new_file18-29.txt', 'w'))

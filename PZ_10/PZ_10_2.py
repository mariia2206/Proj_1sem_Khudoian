# Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое, количество символов в тексте.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей.

print(open('text18-29.txt').read(), '\n' + str(len(open('text18-29.txt').read())))
print(open('text18-29.txt').read().splitlines()[0], '\n' + str(open('text18-29.txt').read().splitlines()[1]), '\n' +
      str(open('text18-29.txt').read().splitlines()[-1]), '\n' + str(open('text18-29.txt').read().splitlines()[2]), '\n' +
      str(open('text18-29.txt').read().splitlines()[3]), '\n' + str(open('text18-29.txt').read().splitlines()[4]), '\n' +
      str(open('text18-29.txt').read().splitlines()[5]), file=open('new_file18-29.txt', 'w', encoding='utf-8'))

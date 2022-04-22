# В исходном текстовом файле (hotline1.txt) найти все номера телефонов, соответствующих шаблону 8(000)000-00-00.
# Посчитать количество полученных элементов.
# После фразы «Горячая линия» добавить фразу «Министерства образования Ростовской области», выполнив манипуляции в новом файле.


import re
reg = re.compile(r"[8]\([0-9][0-9][0-9]\)[0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]")

with open('hotline1.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    fun = list(re.findall(reg, text))
    tur = re.sub(r'«Горячая линия»', '«Горячая линия» «Министерства образования Ростовской области»', text)

print('Количество полученных элементов:', len(fun))

file_2 = open('hotline2.txt', 'w', encoding='utf-8')
file_2.write(tur)


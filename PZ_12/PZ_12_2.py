# -*- coding: utf8 -*-.
# Задача 1 из 5 практической работы 29 варианта.
# Здесь мы импортируем рандом для того чтобы вывести случайные 40 символов.
# Ну и создаем окошко и кнопку с помощью root и button.


from tkinter import *
import random
import string


def various_elements(vvod):
    letters = string.ascii_lowercase + string.digits
    c['text'] = f"40 любых символов: {''.join(random.choice(letters) for i in range(40))}"


root = Tk()
root.title('Генерация 40 любых символов')
root.geometry("700x120")
button1 = Button(text="Сгенерировать")
button1.place(x=300, y=15)
c = Label(font='arial 12')
c.place(x=100, y=40)
button1.bind('<Button-1>', various_elements)
root.mainloop()


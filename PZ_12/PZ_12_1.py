# -*- coding: utf8 -*-
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу.
# Ссылка на интерфейс: https://files.codegrape.com/62259/screenshot2.png.
# Здесь с помощью combobox делаем выпадающий список.
# А BOLD делает шрифт жирным.


from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox

root = Tk()
root.geometry('799x747')
root['bg'] = 'white'
Canvas(root, bg='white', height=750, width=550).place(x=130, y=-10)
Label(text='Contact Form', bg='white', fg='black', font='arial 22').place(x=150, y=0)
Label(text='Name', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=65)
Entry(textvariable=StringVar(value='First & Last Name'), bd=2, width=56, fg='gray', font='arial 12').place(x=145, y=95)
Label(text='Email', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=150)
Entry(textvariable=StringVar(value='Email'), bd=2, width=56, fg='gray', font='arial 12').place(x=145, y=175)
Label(text='Phone Number', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=225)
Entry(textvariable=StringVar(value='Phone Number'), bd=2, width=56, fg='gray', font='arial 12').place(x=145, y=255)
Label(text='Subject', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=305)
combo = Combobox(root, width=40, values=['French','English','Russian','Spanish'])
combo.current(0)
combo.place(x=145, y=335)
Label(text='Leave us a few words', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=385)
Entry(bd=2, width=13, fg='gray', font='arial 53').place(x=145, y=415)
Label(text='File Attachements', bg='white', fg='black', font=('arial', 12, BOLD)).place(x=145, y=515)
Canvas(root, bg='#fff', height=30, width=512).place(x=145, y=545)
Button(text="Choose Files").place(x=153, y=548)
Label(text='No file chosen', bg='white', fg='gray', font='arial 11').place(x=235, y=549)
Canvas(root, bg='#fff', height=80, width=300).place(x=145, y=595)
Canvas(root, bg='#fff', height=25, width=25).place(x=153, y=620)
Label(text='Im not a robot', bg='white', fg='black', font='arial 11').place(x=190, y=623)
Button(text="Submit", width=8, fg='white', bg='#36c').place(x=145, y=690)
root.mainloop()

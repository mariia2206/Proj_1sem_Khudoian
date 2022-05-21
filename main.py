import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#ecd8e9', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#c38bbf', width=184, bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12 .gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#c38bbf',width=184,
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#c38bbf', width=184,
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи",
                               command=self.open_search_dialog, bg='#c38bbf', width=184,
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#c38bbf', width=184,
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('id','full_name_master','clients_full_name','type_of_cleaning','cost','discount'), height=15, show='headings')

        self.tree.column('id', width=40, anchor=tk.CENTER)
        self.tree.column('full_name_master', width=220, anchor=tk.CENTER)
        self.tree.column('clients_full_name', width=220, anchor=tk.CENTER)
        self.tree.column('type_of_cleaning', width=140, anchor=tk.CENTER)
        self.tree.column('cost', width=140, anchor=tk.CENTER)
        self.tree.column('discount', width=140, anchor=tk.CENTER)

        self.tree.heading('id', text='id')
        self.tree.heading('full_name_master', text='ФИО мастера')
        self.tree.heading('clients_full_name', text='ФИО клиента')
        self.tree.heading('type_of_cleaning', text='Тип чистки')
        self.tree.heading('cost', text='Стоимость')
        self.tree.heading('discount', text='Скидка')

        self.tree.pack()

    def records(self, id, full_name_master, clients_full_name,type_of_cleaning, cost, discount):
        self.db.insert_data(id, full_name_master, clients_full_name, type_of_cleaning, cost, discount)
        self.view_records()

    def update_record(self, id, full_name_master, clients_full_name, type_of_cleaning, cost, discount):
        self.db.cur.execute("""UPDATE uslugi1 SET id=?, full_name_master=?, clients_full_name=?, type_of_cleaning=?, cost=?, discount=? WHERE id=?""",
                            (id, full_name_master, clients_full_name, type_of_cleaning,cost, discount, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()

        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM uslugi1 """)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM uslugi1 WHERE id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()


    def search_records(self, cost):
        cost = (cost,)
        self.db.cur.execute("""SELECT * FROM uslugi1 WHERE cost=?""", cost)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()



class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='id')
        label_description.place(x=50, y=0)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=130, y=0, width=100)

        label_description = tk.Label(self, text='ФИО мастера')
        label_description.place(x=50, y=25)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=130, y=25, width=230)

        label_name = tk.Label(self, text='ФИО клиента')
        label_name.place(x=50, y=50)
        self.entry_names = ttk.Entry(self)
        self.entry_names.place(x=130, y=50, width=230)

        label_sex = tk.Label(self, text='Тип чистки')
        label_sex.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'Сухая', u'Аквачистка', u'Ручная', u'Углеводородная'])
        self.combobox.current(0)
        self.combobox.place(x=130, y=75)

        label_old = tk.Label(self, text='Стоимость')
        label_old.place(x=50, y=100)
        self.entry_cost = ttk.Entry(self)
        self.entry_cost.place(x=130, y=100)

        label_score = tk.Label(self, text='Скидка')
        label_score.place(x=50, y=125)
        self.entry_discount = ttk.Entry(self)
        self.entry_discount.place(x=130, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_names.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_cost.get(),
                                                                       self.entry_discount.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_names.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_cost.get(),
                                                                          self.entry_discount.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="*Поиск идет по стоимости равной:")
        label_search.place(x=50, y=0)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=155)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')




class DB:
    def __init__(self):

        with sq.connect('himchistka.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS uslugi1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name_master TEXT NOT NULL,
                clients_full_name TEXT NOT NULL,
                type_of_cleaning TEXT NOT NULL DEFAULT 1,
                cost INTEGER,
                discount INTEGER
                )""")

    def insert_data(self,id, full_name_master, clients_full_name, type_of_cleaning, cost, discount):
        self.cur.execute("""INSERT INTO uslugi1(id, full_name_master, clients_full_name, type_of_cleaning, cost, discount) VALUES (?, ?, ?, ?, ?, ?)""",
                             (id, full_name_master, clients_full_name, type_of_cleaning,  cost, discount))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Химчистка")
    root.geometry("950x450+300+200")
    root.resizable(False, False)
    root.mainloop()

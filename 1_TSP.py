from tkinter import *
import os
from tkinter import messagebox
try:
    os.chdir(r"C:/Program Files/TSPassword")
except:
    newpath = r'C:/Program Files/TSPassword'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def mas(event):
    def edit(event):
        my_file = open("MLP.txt", "a")
        my_file.write("Метка: " +  met.get()  + " Логин: " + log.get()  + " Пароль: " + pas.get() + '\n')
        my_file.close()
        master = Toplevel(root)
        met = StringVar()
        log = StringVar()
        pas = StringVar()
        text_met = Label(master, text="Введи название пароля (метка должна быть уникальной!)")
        text_met.pack()
        ent_met = Entry(master, textvariable=met)
        ent_met.pack()
        text_log = Label(master, text="Введи логин")
        text_log.pack()
        ent_log = Entry(master, textvariable=log)
        ent_log.pack()
        text_pas = Label(master, text="Введи пароль")
        text_pas.pack()
        ent_pas = Entry(master, textvariable=pas)
        ent_pas.pack()
        but = Button(master, text="Создать!")
        but.bind("<Button-1>", edit)
        but.pack()

def search(event):
     def go(event):
         word = s.get()
         filename = 'MLP.txt'
         with open(filename) as f:
             test = print(word if word in f.read() else messagebox.showerror('Error', 'Извини, но я ничего не нашел \nВозможно ты не ввел имя метки…'))
             test = test.str().replace('', '')
         lookup = s.get()
         with open(filename) as myFile:
             for num, line in enumerate(myFile, 0):
                 if lookup in line:
                     num = num
         with open('MLP.txt') as f:
             for index, line in enumerate(f):
                 if index == num:
                     a = line
                     break
             f = open('MLP.txt')
             line = f.readlines()
             test = line[num]

     s = StringVar()
     search = Toplevel(root)
     text = Label(search, text="Введи метку")
     text.pack()
     ent = Entry(search, textvariable=s)
     ent.pack()
     but = Button(search, text="Искать")
     but.bind("<Button-1>", go)
     but.pack()

def settings(event):
    def BS(event):
        os.chdir(message.get())
        message = StringVar()
        help = Label(Set, text="Введи директорию, (Пример: C:" + '/' + "test)")
        help.pack()
        ent = Entry(Set, textvariable=message)
        ent.pack()
        but = Button(Set, text = "Изменить")
        but.bind("<Button-1>", S)
        but.pack()
    Set = Toplevel(root)
    but_set = Button(Set, text="Директория паролей")
    but_set.place(relx=.5, rely=.1, anchor="c", height=30, width=130, bordermode=OUTSIDE)
    but_set.bind("<Button-1>", BS)


root = Tk()
root.geometry("370x250")

text = Label(text="Добро пожаловать!")
text.place(relx=.4, rely=.1, anchor="c", height=30, width=130, bordermode=OUTSIDE)
but = Button(text="Настройки")
but.place(relx=.8, rely=.1, anchor="c", height=30, width=130, bordermode=OUTSIDE)
but.bind("<Button-1>", settings)
butmas = Button(root, text="Создать пароль")
butmas.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
butmas.bind("<Button-1>", mas)
but_s = Button(root, text="Поиск пароля")
but_s.bind("<Button-1>", search)
but_s.place(relx=.5, rely=.7, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()

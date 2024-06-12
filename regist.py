from tkinter import *
from tkinter import ttk
import os
import mysql.connector
from tkinter.messagebox import showinfo, showerror

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="comicsans21",
    database="diplomwork",
    charset="utf8",
    use_unicode=True
)

mycursor = mydb.cursor()

def register():
    username = entry_username.get()
    password = entry_password.get()

    mycursor.execute("INSERT INTO data (user, passw) VALUES (%s, %s)", (username, password))
    mydb.commit()
    showinfo("Успешная регистрация", "Регистрация выполнена успешно!")

root = Tk()
root.title("Регистрация")
root.geometry("200x200+600+250")
root.resizable(False, False)

label_username = Label(root, text="Имя пользователя:")
label_username.pack()
entry_username = Entry(root)
entry_username.pack()

label_password = Label(root, text="Пароль:")
label_password.pack()
entry_password = Entry(root, show="*")
entry_password.pack()


btn_register = Button(root, text="Зарегистрироваться", command=register)
btn_register.pack()

root.mainloop()



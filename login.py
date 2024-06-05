from tkinter import *
from tkinter import ttk
import os
import mysql.connector
from tkinter.messagebox import showinfo, showerror

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="comicsans21",
    database="diplomwork"
)

mycursor = mydb.cursor()

def create_window():
    os.system('python main1.py')


def show_info():
    showinfo(title="Информация", message="Успешный вход")

def show_info1():
    show_info1(title="Информация", message="Пользователь удален")

def show_error():
    showerror(title="Ошибка", message="Сообщение об ошибке")


def login():
    username = entry_username.get()
    password = entry_password.get()

    mycursor.execute("SELECT * FROM data WHERE user = %s AND passw = %s", (username, password))
    result = mycursor.fetchall()

    if result:
        showinfo("Успешный вход", "Вход выполнен успешно!")
        create_window()
        root.destroy()
    else:
        showerror("Ошибка", "Неверное имя пользователя или пароль")


def register():
    username = entry_username.get()
    password = entry_password.get()

    mycursor.execute("INSERT INTO data (user, passw) VALUES (%s, %s)", (username, password))
    mydb.commit()
    create_window()
    showinfo("Успешная регистрация", "Регистрация выполнена успешно!")


root = Tk()
root.title("Вход и регистрация")
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

btn_login = Button(root, text="Войти", command=login)
btn_login.pack()

btn_register = Button(root, text="Зарегистрироваться", command=register)
btn_register.pack()

root.mainloop()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="comicsans21",
    database="diplomwork",
    charset="utf8",
    use_unicode=True
)

mycursor = mydb.cursor()

def create_window():
    os.system('python main1.py')


root.mainloop()

# Вариант 10 username corefx
from tkinter import *
from tkinter import ttk
import requests
import json
from pprint import pprint

root = Tk()  # создаем корневой объект - окно
root.title("Кравцов Н.Р.")  # устанавливаем заголовок окна
root.geometry("350x350")  # устанавливаем размеры окна

label2 = ttk.Label(text="Введите имя репозитория")
label2.pack(anchor=NW, padx=6, pady=6)

operand1 = ttk.Entry()
operand1.pack(anchor=NW, padx=6, pady=6)



def write_file():
    # Имя пользователя github
    #username = "kubernetes"
    username2 = operand1.get();
    # url для запроса
    url = f"https://api.github.com/users/{username2}"
    # делаем запрос и возвращаем json
    user_data = requests.get(url).json()

    parametrs = ['company', 'created_at', 'email', 'id', 'name', 'url']

    result = {}
    for i in range(len(parametrs)):
        result[parametrs[i]] = user_data[parametrs[i]]
    pprint(result)
    with open("TestResult.json", "w") as f:
        json.dump(result, f, indent = 4)
#pprint(user_data)

result = ttk.Button(text="Результат", command = write_file)
result.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
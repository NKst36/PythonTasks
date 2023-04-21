from tkinter import *
from tkinter import ttk
from tkinter import filedialog
root = Tk()  # создаем корневой объект - окно
root.title("Кравцов Н.Р.")  # устанавливаем заголовок окна
root.geometry("350x350")  # устанавливаем размеры окна

#s = ttk.Style()
#s.configure('TNotebook', tabposition='nw')

label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем фреймы для калькулятора, чекбоксов и загрузки текста из файла
calculator = ttk.Frame(notebook)
#calculator.grid(sticky = (E,W))
check_box = ttk.Frame(notebook)
#check_box.grid(sticky = (E,W))
text_load = ttk.Frame(notebook)
#text_load.grid(sticky = (E,W))


calculator.pack(fill=BOTH, expand=True)
check_box.pack(fill=BOTH, expand=True)
text_load.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(calculator, text="Калькулятор")
notebook.add(check_box, text="Чекбоксы")
notebook.add(text_load, text="Загрузка текста из файла")

# Калькулятор
# Надпись для первого операнда
label1 = ttk.Label(calculator, text = "Введите первый операнд")
label1.pack(anchor=NW, padx=6, pady=6)

# Поле ввода первого операнда
operand1 = ttk.Entry(calculator)
operand1.pack(anchor=NW, padx=6, pady=6)

# Выбор действия
# Надпись выбора действия
label2 = ttk.Label(calculator, text = "Выберите действие")
label2.pack(anchor=NW, padx=6, pady=6)

# combobox
activity = ["+", "-", "*", "/"]
combobox = ttk.Combobox(calculator, values = activity)
combobox.pack(anchor=NW, padx=6, pady=6)

# Надпись для второго операнда
label3 = ttk.Label(calculator, text = "Введите второй операнд")
label3.pack(anchor=NW, padx=6, pady=6)

# Поле ввода второго операнда
operand2 = ttk.Entry(calculator)
operand2.pack(anchor=NW, padx=6, pady=6)

# Вывод результата
#result_output = ttk.Label(calculator, text = "Hello")
#result_output.pack(anchor=NW, padx=6, pady=6)

#Введенные данные
# Это это не работает
first_operand = operand1.get()
second_operand = operand2.get()
operator = combobox.get()
# Функции калькулятора

def sum():
    return float(operand1.get()) + float(operand2.get())

def subtract():
    return float(operand1.get()) - float(operand2.get())

def multiply():
    return float(operand1.get()) * float(operand2.get())

def divide():
    return float(operand1.get()) / float(operand2.get())

#Список функций
dictionary_func = {
        "+": sum,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

preview_result = ttk.Label(calculator, text = "Результат")
preview_result.pack(anchor=NW, padx=6, pady=6)

def calculate():
    myfunc = dictionary_func.get(combobox.get())
    preview_result.config(text = myfunc())

result = ttk.Button(calculator, text = "Результат", command = calculate)
result.pack(anchor=NW, padx=6, pady=6)


# Task 2 Checkbox
def select():
    myresult = []
    if first.get() == 1: myresult.append("first")
    if second.get() == 1: myresult.append("second")
    if third.get() == 1: myresult.append("third")
    result = ", ".join(myresult)
    if not myresult: result = "No checkbox is selected"
    checkboxs.set(result)

position = {"padx": 6, "pady": 6, "anchor": NW}

checkboxs = StringVar()
result_label = ttk.Label(check_box, textvariable=checkboxs)
result_label.pack(**position)

first = IntVar()
first_checkbutton = ttk.Checkbutton(check_box, text="first", variable=first)
first_checkbutton.pack(**position)

second = IntVar()
second_checkbutton = ttk.Checkbutton(check_box, text="second", variable=second)
second_checkbutton.pack(**position)

third = IntVar()
third_checkbutton = ttk.Checkbutton(check_box, text="third", variable=third)
third_checkbutton.pack(**position)

btn = ttk.Button(check_box, text = "Выполнить", command = select)
btn.pack(anchor=NW, padx=6, pady=6)

# Task 3 file
#Третья вкладка: работа с текстом, можно текст загрузить
#файла по кнопке из созданного вами меню.
#text_editor = Text(text_load)
#text_editor.pack(anchor=NW, padx=6, pady=6)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding = "utf-8") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)

root.option_add("*tearOff", FALSE)

main_menu = Menu()
file_menu = Menu()

#file_menu.add_command(label="New")
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Open", command = open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

text_editor = Text(text_load)
text_editor.pack()

root.config(menu=main_menu)
root.mainloop()

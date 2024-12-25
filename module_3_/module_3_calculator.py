#'Калькулятор'
import tkinter as tk



def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2



def insert_values(values):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)



def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)



def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)



def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)



window = tk.Tk()

window.title("Калькулятор") # Имя окна
window.geometry("350x350") # Размер окна
window.resizable(False, False) # Растягивать запрещено

button_add = tk.Button(window, text=" + ", width=2, height=1, command=add)
button_add.place(x=10, y=200)

button_sub = tk.Button(window, text=" - ", width=2, height=1, command=sub)
button_sub.place(x=40, y=200)

button_mul = tk.Button(window, text=" * ", width=2, height=1, command=mul)
button_mul.place(x=70, y=200)

button_div = tk.Button(window, text=" / ", width=2, height=1, command=div)
button_div.place(x=100, y=200)

number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=10, y=10)
number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=10, y=40)

number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=10, y=70)
number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=10, y=100)

answer = tk.Label(window, text="Результат:")
answer.place(x=10, y=130)
answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=10, y=160)

window.mainloop()
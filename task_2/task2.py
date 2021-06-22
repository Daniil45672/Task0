from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys



#Зовнішній вигляд
root = Tk() 
root.title("Калькулятор")
bttn_list = [
"bin", "AC","+/-", "%" ,
"7", "8", "9", "+",
"4", "5", "6", "-", 
"1", "2", "3", "*",
"0", ".", "=",  "/",
"(", ")",   
"sin", "cos", "tan" ,
"ctg" , "log","ln", ]
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10 ).grid(row=r, column = c)
    c += 1
    if c > 3:
        c = 0
        r += 1
calc_entry = Entry(root, width = 30)
calc_entry.grid(row=0, column=0, columnspan=4)
def calc(key):
    global memory
    if key == "=":
#Буде виводити якщо не правильно буде записано
        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Перший символ - це не число!")
            messagebox.showerror("Ошибка!", "Ви не ввели число!")
#Розрахунки
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!", "Перевірте правильність даних")
#Видалення результату
    elif key == "AC":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "tan":
        calc_entry.insert(END, "=" + str(math.tan(int(calc_entry.get()))))
    elif key == "ctg":
        calc_entry.insert(END, "=" + str((math.cos(int(calc_entry.get()))/(math.sin(int(calc_entry.get()))))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "log":
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()))))
    elif key == "ln":
        calc_entry.insert(END, "=" + str(math.log10(int(calc_entry.get()))))
    elif key == "%":
        calc_entry.insert(END, "=" + str(int(calc_entry.get())*(int(calc_entry.get())/100)))
    elif key == "bin":
        calc_entry.insert(END, "=" + bin(int(calc_entry.get())))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
        root.mainloop()


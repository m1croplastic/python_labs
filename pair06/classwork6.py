import math
from math import *
import statistics as stat
import random
from datetime import date
import demo
from tkinter import *
#
# print(math.sqrt(64))
#
# a = [10, 15, 90, 100]
# print(f"Середній бал: {stat.mean(a)}")
# r = int(input("r = "))
# circle_area = pi * pow(r, 2)
# print(round(circle_area, 2))



# ball = 25
# cap = 6
# print(f"Повністю заповнених: {floor(ball/cap)}")
# print(f"Всього: {ceil(ball/cap)}")



# num = []
# for i in range(10):
#     num.append(random.randint(1,100))
# print(num)
#
# select = random.choice(num)
# print(select)



# print(f"Сьогодні: {date.today()}")



# print(demo.square(5))
# print(demo.is_even(5))
# grades = [3, 8, 6, 5]
# print(demo.average(grades))

def text():
    text = "Hello World"
    lbl_text["text"] = text
def clear():
    lbl_text["text"] = ""

window = Tk()
window.title("omg i can open a window")
window.geometry("500x400")
window.resizable(width=False, height=False)
window["bg"] = "#7FFFD4"
label = Label(window, text="Я кампутєрний гєній", font = ("Arial", 36), bg = "#CCCCFF", pady = 20)
label.pack()
# label.place(x=20, y=20)
frame = Frame(window)
frame.pack()
button1 = Button(frame, text = "OK🥰🥰🥰", width = 15, activebackground="lavender")
button1.grid(row = 0, column = 0, padx = 10)
button2 = Button(frame, text = "NOT OK😡🤬", width = 15, activebackground="lavender")
button2.grid(row = 0, column = 1, padx = 10)
button2.bind("<Button-1>", clear)
lbl_text = Label(frame, text = text, font = ("Arial", 36), bg = "#CCCCFF", pady = 20)
lbl_text.grid(row = 1, column = 0, columnspan=2)
window.mainloop()
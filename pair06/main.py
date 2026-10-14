import student_utils
from tkinter import *
students = input("Введіть імена учнів через кому: ").split(",")
print(students)
count = int(input("Введіть кількість оцінок: "))
for student in students:
    grades = student_utils.generate_grades(count)
    average = student_utils.average_grade(grades)
    level = student_utils.get_level(average)
    print(f"{student}: {grades} - {average} - {level}")

window = Tk()
window.title("Статистика учнів")
label = Label(window, text="Оцінки учнів і відомості про них", font = ("Arial", 25), bg = "#CD00CD", pady = 20)
label.pack()
entry = Entry(window, width = 20, font = ("Arial", 25))
entry.pack()
if entry.get().isdigit():
   count = int(entry.get())
frame = Frame(window)
frame.pack()
button1 = Button(frame, text="Сформувати звіт", width=15, activebackground="#CD00CD")
button1.pack()


window.mainloop()
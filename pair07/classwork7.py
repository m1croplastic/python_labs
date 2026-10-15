import os

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування.\n")
        file.write("Python використовується для роботи з даними.\n")
        file.write("Файли дозволяють зберігати інформацію\n")
        file.write("Python вимагає практики.\n")
        file.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists('numbers.txt.txt'):
    with open('numbers.txt.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")


# with open('hello.txt', 'w', encoding="utf-8") as file:
#     file.write("Hello world\n")
#     file.write("Hello world2\n")
#     file.write("Hello world3\n")

# w - режим запису(файл перезаписується)
# r - режим читання(тільки якщо файл вже існує)
# a - додає текст в кінець, старий вміст не стирається
# x - створення нового файлу(якщо існує помилка)


# with open("text.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# print(f"read() => \n{text}, \nlen() => {len(text)}")


# with open("text.txt", "r", encoding="utf-8") as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     other_lines = file.readlines()
# print(line1)
# print(line2)
# print(other_lines)


# with open("text.txt", "r", encoding="utf-8") as file:
#     for number, line in enumerate(file, start = 1):
#         clean_line = line.strip()
#         print(f"{number}. {clean_line}")


# line = "olesia pirivit;2\n"
# clean_line = line.strip()
# name, grade = clean_line.split(';')
# print(name)
# print(grade)


# students = []
# umni = []
# with open('students.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         name, grade = line.strip().split(';')
#         students.append([name, grade])
#         if int(grade) >= 90:
#             umni.append([name, grade])
# print(students)
# print(umni)
# with open('umni.txt', 'w', encoding="utf-8") as file:
#         for name, grade in umni:
#             file.write(name + ';' + grade + '\n')


grades = []
with open("grades.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, subject, grade = line.strip().split(' ')
        grades.append(grade)
        print(name, subject, grade)
average = sum(grades) / len(grades)
print(average)
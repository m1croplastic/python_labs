# 1
#
# while True:
#     try:
#        a = float(input("Введіть 1 число: "))
#        break
#     except ValueError:
#        print("Некоректно введене число")
#
# while True:
#     try:
#        b = float(input("Введіть 2 число: "))
#        break
#     except ValueError:
#        print("Некоректно введене число")
# diya = input("Введіть дію(+, -, *, /): ").strip()
# if diya == "+":
#     print(f"{a} + {b} = {a+b}")
# elif diya == "-":
#     print(f"{a} - {b} = {a-b}")
# elif diya == "*":
#     print(f"{a} * {b} = {a*b}")
# elif diya == "/":
#     if b == 0:
#         print("Ділити на 0 не можна")
#     else:
#         print(f"{a} / {b} = {a/b}")
# else:
#     print("Невідома дія")



# 2
#
# def input_grade():
#     while True:
#         try:
#             g = int(input("Введіть оцінку(1-12): "))
#             if g<1 or g>12:
#                 raise ValueError("Оцінка повинна бути від 1 до 12")
#             return g
#         except ValueError as e:
#             print(e)
# print(f"Прийнято: {input_grade()}")



# 3
#
# student = ["Захуцька Олеся", "Мельник Діана", "Кобець Артем", "Бушмакін Вадим", "Желєй Ярослав"]
# grade = {
#     "біологія": 8,
#     "фізика": 6,
#     "геометрія": 11,
#     "укр. літ": 9,
#     "інформатика": 4
# }
# print("1 - пошук учня за індексом")
# print("2 - оцінка за назвою предмета")
# choice = input("Що обираєте?:").strip()
# if choice == "1":
#     print(student)
#     try:
#        search = int(input("Введіть індекс учня(0-4): "))
#        if search < 0:
#            print("Індекс не може бути від'ємним")
#        else:
#            print(f"{search}: {student[search]}")
#     except ValueError:
#         print("Ви ввели нечисловий індекс")
#     except IndexError:
#         print("Нема учня з таким індексом")
# elif choice == "2":
#     search = input("Введіть назву предмета: ").strip().lower()
#     try:
#         print(f"Оцінка з предмета {search}: {grade[search]}")
#     except KeyError:
#         print("Такого предмета немає в списку")
# else:
#     print("Виберіть опцію 1 або 2")



# 4
#
# report = []
# right = 0
# wrong = 0
# try:
#    with open("students.txt", "r", encoding="utf-8") as file:
#       for number, line in enumerate(file, start=1):
#             part = line.split(";")
#             if len(part) != 2:
#               print(f"У рядку {number} немає роздільника «;» або кількість полів неправильна")
#               wrong += 1
#               continue
#
#             name = part[0]
#             try:
#                 grade = int(part[1])
#             except ValueError:
#                 print(f"У рядку {number} введена оцінка не є цілим числом")
#                 wrong += 1
#                 continue
#
#             if grade < 0 or grade > 100:
#                 print(f"У рядку {number} введена оцінка виходить за межі дозволеного")
#                 wrong += 1
#                 continue
#             report.append((name, grade))
# except FileNotFoundError:
#     print("Файл students.txt не знайдено")
#
# report.sort(key=lambda x: x[1], reverse=True)
# with open("report.txt", "w", encoding="utf-8") as f:
#     for name, grade in report:
#         f.write(f"{name};{grade}\n")
#
# print(f"Правильних рядків: {right}")
# print(f"Пропущених рядків: {wrong}")
# print("Створено report.txt")
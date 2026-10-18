# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print("Please enter a valid age")
#ValueError - тип операції правильний, але значення не можна використати



# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     result = a / b
#     print(result)
# except ValueError:
#     print("a і b повинні бути числами")
# except ZeroDivisionError:
#     print("Ділити на 0 не можна")
# finally: print("Програму завершено")



# while True:
#      try:
#          grade = int(input("Enter your grade: "))
#          if grade < 1 or grade > 12:
#              raise ValueError("Invalid Grade")
#          print(f"Grade: {grade}")
#          break
#      except ValueError as error_limit:
#          print(f"Error: {error_limit}")



# def int_input(message):
# 	while True:
# 		try:
# 			return int(input(message))
#         except ValueError:
#                print("Please enter an integer")
#
# n = int_input("Please enter a number")
# print(n)



# def input_grade():
#     while True:
#         try:
#             grade = int(input("Enter your grade: "))
#             if grade < 1 or grade > 12:
#               raise ValueError("Grade must be between 1 and 12")
#             return grade
#         except ValueError as error:
#             print(error)
#
# grade = input_grade()
# print(f"Оцінка {grade} прийнята")



# price = {
#     "apple": 50,
#     "orange": 70,
#     "banana": 90,
# }
# product = input("Enter product name: ")
# try:
#    print(price[product])
# except KeyError:
#     print("Продукт не знайдено")
#
# product = input("Enter product name: ")
# price = price.get(product, "товару немає")



# try:
#     with open("data.txt", "r", encoding="utf-8") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("Файл не знайдено")


# line = "Ivan;95"
# parts = line.strip().split(";")
# if len(parts) != 2:
#     print("Помилка у рядку")
# else:
#     name = parts[0]
#     grade = parts[1]
#
#     try:
#         grade_int = int(grade)
#         if grade_int < 0 or grade_int > 100:
#             raise ValueError("Не той бал")
#     except ValueError as e:
#         print(f"Помилка {e}")
#     else:
#         print(f"Правильний запис: {name} - {grade_int}")



lines = [
    "Ivan;95",
    "Liza;hello",
    "Vadym;100"
]
for line_number, line in enumerate(lines, start=1):
    parts = line.strip().split(";")
    if len(parts) != 2:
        print(f"Рядок {line_number} має помилку")
        continue
    name = parts[0]
    try:
        score = int(parts[1])
    except ValueError:
        print(f"Рядок {line_number} пропущено, бал виставлено неправильно")
        continue
    print(f"Правильний запис {name} - {score}")
# 1
#
# def s_circle(r):
#     return 3.14159 * r
#
# def s_rectangle(width, height):
#     return width * height
#
# def s_triangle(width, height):
#     return width * height * 0.5
#
# def main():
#     print("Оберіть фігуру:")
#     print("1 — Круг")
#     print("2 — Прямокутник")
#     print("3 — Трикутник")
#     choice = input("Ваш вибір: ")
#
#     if choice == "1":
#         r = float(input("Радіус: "))
#         result = s_circle(r)
#         print("Площа круга:", result)
#
#     elif choice == "2":
#         height = float(input("Висота: "))
#         width = float(input("Ширина: "))
#         result = s_rectangle(width, height)
#         print("Площа прямокутника:", result)
#
#     elif choice == "3":
#         width = float(input("Сторона: "))
#         height = float(input("Висота до сторони: "))
#         result = s_triangle(width, height)
#         print("Площа трикутника:", result)
#
#     else:
#         print("Не ті цифєрки")
#
# main()






# 3
#
# grade = input("Введіть оцінки через пробіл: ")
# grades_list = [int(g) for g in grade.split()]
#
# def average(grades):
#     return sum(grades) / len(grades)
#
# def minimum(grades):
#     return min(grades)
#
# def maximum(grades):
#     return max(grades)
#
# def count_above(grades):
#     count = 0
#     value = int(input("Введіть оцінку для порівняння: "))
#     for g in grades:
#         if g > value:
#             count += 1
#     return count
#
# def print_report(grades):
#     print("Середній бал:", round(average(grades)))
#     print("Найкраща оцінка:", maximum(grades))
#     print("Найгірша оцінка:", minimum(grades))
#     print("Вище заданого:", count_above(grades))
#
# def main():
#     grades = grades_list
#     print_report(grades)
#
# main()






# 4
#
# password = input("Введіть пароль: ")
# def min_length(password):
#     if len(password) < 8:
#         print("Недостатня довжина")
#     else:
#         return password
# def has_number(password):
#     count = 0
#     for p in password:
#         if p.isdigit():
#             count += 1
#     if count == 0:
#         print("Не містить цифри")
#     else:
#         return password
# def has_upper(password):
#     count = 0
#     for p in password:
#         if p.isupper():
#             count += 1
#     if count == 0:
#         print("Не містить великої літери")
#     else:
#         return password
# def has_lower(password):
#     count = 0
#     for p in password:
#         if p.islower():
#             count += 1
#     if count == 0:
#         print("Не містить малої літери")
#     else:
#         return password
# def has_special(password):
#     if password.isalnum() == True:
#         print("Не містить спеціального символа")
#     else:
#         return password
#
# def validate_password(password):
#     min_length(password)
#     has_number(password)
#     has_upper(password)
#     has_lower(password)
#     has_special(password)
#
# validate_password(password)
# 1
#
# import math
#
# r = float(input("Введіть радіус для обчислення площі круга: "))
# circle = math.pi * pow(r, 2)
# print(round(circle,2))
#
# side1 = float(input("Введіть довжину 1 катета: "))
# side2 = float(input("Введіть довжину 2 катета: "))
# hypot = math.sqrt(pow(side1, 2) + pow(side2, 2))
# print(round(hypot,2))
#
# things = int(input("Введіть кількість предметів: "))
# capacity = int(input("Введіть місткість 1 коробки: "))
# count = math.ceil(things / capacity)
# print(round(count,2))




# 2
#
# import random
# import statistics
#
# count = int(input("Введіть кількість оцінок: "))
# num = []
# level3 = 0
# if count > 0:
#     for i in range(count):
#         num.append(random.randint(1, 12))
# else:
#     print("Неможлива кількість оцінок")
#     exit()
# for n in num:
#     if n>=10:
#         level3 += 1
# print(f"Оцінки: {num}")
# print(f"Максимальна оцінка: {max(num)}")
# print(f"Мінімальна оцінка: {min(num)}")
# print(f"Середня оцінка: {statistics.mean(num)}")
# print(f"Медіана оцінок: {statistics.median(num)}")
# print(f"Кількість оцінок високого рівня: {level3}")




# 3
#
# import datetime
#
# day = int(input("Введіть день події: "))
# month = int(input("Введіть місяць події: "))
# year = int(input("Введіть рік події: "))
# podiya = datetime.date(year, month, day)
# today = datetime.date.today()
# print(podiya)
# if podiya > today:
#    rizn = podiya - today
#    print(f"До події залищилось {rizn}")
# elif podiya < today:
#     rizn = today - podiya
#     print(f"Подія сталась стільки днів тому: {rizn}")
# else:
#     print("Цей день сьогодні!")




4


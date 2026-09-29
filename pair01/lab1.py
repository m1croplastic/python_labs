# №1

# (a)
# a = int(input("Введіть ціле число: "))
# if a/2 == int(a/2):
#     print("Число парне")
# else: print("Число непарне")

# (b)
# b = int(input("Ваш вік: "))
# if b >= 18:
#     print("Ви повнолітні!")
# else: print("Ви неповнолітні!")

# (c)
# c = float(input("Радіус кола: "))
# print(f"Площа круга: {c**2}π")
# print(f"Довжина кола: {2*c}π")

# (d)
# a = float(input("Число a: "))
# b = float(input("Число b: "))
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else: print("Числа рівні")


# №2

# x, y = input("Введіть координати точки: ").split( )
# x = int(x)
# y = int(y)
# if x>0 and y>0: print("Точка знаходиться у 1 чверті")
# elif x<0 and y>0: print("Точка знаходиться у 2 чверті")
# elif x<0 and y<0: print("Точка знаходиться у 3 чверті")
# elif x>0 and y<0: print("Точка знаходиться у 4 чверті")
# else: print("Точка знаходиться на перетині чвертей")


# №3

# x = int(input("Ваш вік: "))
# if x > 120 or x < 0:
#     print("Брехня, давай заново")
# elif 10<x<20:
#     print(f"{x} років")
# elif x%10 == 5 or x%10 == 6 or x%10 == 7 or x%10 == 8 or x%10 == 9 or x%10 == 0:
#     print(f"{x} років")
# elif x%10 == 1:
#     print(f"{x} рік")
# elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
#     print(f"{x} роки")
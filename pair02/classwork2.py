# 1 виконання тіла циклу - ітерація
# range() може мати від 1 до 3 аргументів
# for i in range(5):
#     i = i+1
#     print(i)
# інкремент - збільш. на 1 ; декремент - зменш. на 1
# for i in range(1, 11, 2):
#     print(i)

# for i in range(5):
#     i = i+1
#     print(i)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# suma = 0
# n = int(input())
# for i in range(1, n + 1):
#     suma += i
# print(suma)

# f = 1
# n = int(input())
# for i in range(1, n + 1):
#     f *= i
# print(f)

# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1
# print(count)

# while True:
#     n = int(input("Введи число, для виходу введи 0: "))
#     if n == 0:
#         break
#     print(n)

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#        print(i)

# n = 948375948
# suma = 0
# while n > 0:
#       digit = n % 10
#       suma += digit
#       n = n // 10
# print(suma)

# n = 8946399
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n = n // 10
# print(max_digit)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# width = 8
# height = 6
#
# for row in range(height):
#     for col in range(width):
#         print("*", end="")
#     print()
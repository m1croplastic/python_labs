# 1
#
# n = int(input("Введіть натуральне число: "))
# suma = 0
# count = 0
#
# for i in range(1,n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
#         count += 1
# if count > 0:
#     ser = suma/count
#     print(f"Кількість: {count}")
#     print(f"Сума: {suma}")
#     print(f"Середнє: {ser}")


# 2
#
# n = int(input("Введіть натуральне число: "))
# count = 0
# suma = 0
# max_dig = 0
# min_dig = 0
# while n > 0:
#     dig = n % 10
#     suma += dig
#     count += 1
#     if dig > max_dig:
#         max_dig = dig
#     if dig < min_dig:
#         min_dig = dig
#     n //= 10
# print(f"Кількість цифр: {count}")
# print(f"Сума цифр: {suma}")
# print(f"Найбільша цифра: {max_dig}")
# print(f"Найменша цифра: {min_dig}")


# 3
#
# n = int(input("Введіть натуральне число: "))
# for i in range(1,n+1):

# 4
#
# width = int(input("width: "))
# height = int(input("height: "))
# cont = input("контур: ")
# inside = input("всередині: ")
# if width >= 3 and height >= 3:
#     for row in range(height):
#         for col in range(width):
#             if row == 0 or col == 0 or row == height - 1 or col == width - 1:
#                print(cont, end="")
#             else:
#                print(inside, end="")
#         print()
# else:
#     print("нізя")

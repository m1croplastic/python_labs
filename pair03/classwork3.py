# name = "Olesia"
# age = "16"
# print(len(name))
# print(name[5])
# print(len(name)-1)
from itertools import count

# text = input()
# if len(text) > 0:
#     print(text[0])
# else:
#     print("No text")

# text = "hello world"
# print(text[:5])
# print(text[6:])
# print(text[::2])
# print(text[::-1])
#
# стрінговий тип - незмінна колекція(не можна перезаписувати)
#
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# text = "           kkk       "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# user_login = "admin"
# login = input("Enter your login name: ").strip().lower()
# if user_login == "login":
#     print("Welcome " + user_login)

# text = "Python"
# for char in text:
#     print(char)

# password = input()
# digits = 0
# upper_letter = 0
# if len(password) >= 8:
#     for char in password:
#         if char.isdigit():
#             digits += 1
#         if char.isupper():
#             upper_letter += 1
#         if digits >= 2 and upper_letter >= 2:
#             print("Пароль надійний")
# else:
#     print("Пароль не надійний")
#
# password.isdigit()
# password.isupper()
# password.islower()
# password.isalpha()
# password.isalnum()

# golosni = "уєиїоуяію"
# text = input("Введи текст: ").lower()
# for char in text:
#     if char in golosni:
#         count += 1
# print(count)

# text = "helo vorld ! paiton is ze best!!"
# words = text.split()
# print(words)
# result = "-".join(words)
# print(result)
# new_text = text.replace("python", "java")

# text = input().lower().strip()
# if text == text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# text = input().strip()
# words = text.split()
# max_w = words[0]
# for w in words[1:]:
#     if len(w) > len(max_w):
#         max_w = w
# print(max_w)
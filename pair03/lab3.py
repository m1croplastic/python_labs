# 1
#
# text = input("Введіть текст: ").lower()
# chars = len(text)
# words = len(text.split())
# letters = 0
# golos = 0
# numbers = 0
# spaces = 0
# golosni = "aeiou"
# for char in text:
#      if char in golosni:
#          golos += 1
#      if char.isalpha():
#          letters += 1
#      if char.isdigit():
#          numbers += 1
#      if char.isspace():
#          spaces += 1
# print(f"Символів: {chars}")
# print(f"Літер: {letters}")
# print(f"Цифр: {numbers}")
# print(f"Пробілів: {spaces}")
# print(f"Голосних: {golos}")
# print(f"Слів: {words}")

# 2
#
# pib = input("Введіть ваш ПІБ: ").title().strip()
# part = pib.split()
# if len(part) == 3:
#     prizv = part[0]
#     name = part[1]
#     batko = part[2]
# imya = f"{prizv} {name[0]}.{batko[0]}."
# print(imya)

# 3
#
# pershi = input("1 рядок: ").strip().lower()
# drugi = input("2 рядок: ").strip().lower()
# pershi = pershi.replace(" ", "")
# drugi = drugi.replace(" ", "")
# if pershi == drugi:

# 4
#
# text = input("Введіть речення: ").strip().lower()
# words = text.split()
# max_w = words[0]
# for w in words[1:]:
#      if len(w) > len(max_w):
#          max_w = w
# min_w = words[0]
# for w in words[1:]:
#     if len(w) < len(min_w):
#         min_w = w
# unikalni = 0
# for w in words:
#     if w not in unikalni:
#         unikalni += 1
# old = input("Слово для заміни: ")
# new = input("Нове слово: ")
# new_text = text.replace(old, new)
# print(f"Найдовше: {max_w}")
# print(f"Найкоротше: {min_w}")
# print(f"Унікальних слів: {unikalni}")
# print(f"Після заміни: {new_text}")
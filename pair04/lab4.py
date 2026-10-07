# 1
#
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# dodatni = []
# minusovi = []
# parni = []
# kratni3 = []
# for n in numbers:
#     if n > 0:
#         dodatni.append(n)
#     if n < 0:
#         minusovi.append(n)
#     if n % 2 == 0:
#         parni.append(n)
#     if n % 3 == 0:
#         kratni3.append(n)
# suma = sum(numbers)
# average = suma / len(numbers)
# print(dodatni)
# print(minusovi)
# print(parni)
# print(kratni3)
# print(min(numbers))
# print(max(numbers))
# print(suma)
# print(average)


# 2
#
# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
# spilni = group1 & group2
# only1 = group1 - group2
# only2 = group2 - group1
# vsi = group1 | group2
# print(spilni)
# print(only1)
# print(only2)
# print(vsi)


# 3
#
# products = {
#     "durian": 900,
#     "tualetka": 70,
#     "zoshyt": 25,
#     "catfood": 15,
#     "mochi": 60,
#     "markers": 85
# }
# products["kilo_kartoshki"] = 16
# products["durian"] = 750
# print(products.get("mochi"))
# print(products.get("halva"))
# bazoviy_minimum = int(input("Введіть мінімальну ціну товара: "))
# rozkoshniy_maksimum = int(input("Введіть максимальну ціну товару: "))
# for key, value in products.items():
#     if bazoviy_minimum <= value <= rozkoshniy_maksimum:
#         print(key, value)


# 4
#
# group_info = ("10-IT", "2026/2027")
# grupa = {
#     "Ганищенко Анна Сергіївна": [9, 11, 5, 6, 10],
#     "Гелетюк Дарія Олександрівна": [10, 2, 10, 10, 12],
#     "Захуцька Олеся Миколаївна": [2, 3, 6, 1, 4],
#     "Остапенко Мар'яна Русланівна": [7, 4, 9, 12, 9],
#     "Толстая Єлизавета Анатоліїна": [8, 11, 9, 6, 9]
# }
#
# # це я старалась но шось пішло не так
# # pib = input("Введіть ПІБ нового учня: ")
# # grades = (input("Введіть оцінки учня через кому: "))
# # graddes = grades.split(",")
# # for g in grades:
# #     type(g) == int(g)
# # grupa[pib] = graddes
# # print(grupa)
#
# print(group_info)
# print(grupa)
# for key, value in grupa.items():
#    if len(value) == 5:
#        seredni = sum(value)/5
#        print(key, seredni)
#    else:
#        print("Мало оцінок")
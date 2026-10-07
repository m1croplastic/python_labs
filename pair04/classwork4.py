#колекції - структури даних, що зберігають в собі набори значень

#list - список(впорядкована змінна колекція)
# grades = [12, 8, 10, "2"]
# numbers =  []
# numbers2 = list()
# print(grades[2])
# print(len(grades))
# print(grades[len(grades)-1]) #вивести ост. елемент списку
# numbers.append(6)
# numbers.append("11")
# numbers.insert(1,44)
# numbers.extend([77, "0", 5])
# numbers.remove("0")
# if 12 in numbers:
#     numbers.remove("0")
#
# numbers.pop(-1) #видалення за індексом
# del numbers[1]

# numbers.clear()
# print(numbers.count(6))
# print(numbers.index(6))
# print(numbers)
# print(20 in numbers)
# print(min("a", "b", "c")) #зі стр по алфавіту
# if len(numbers) > 0:
#     average = sum(numbers) / len(numbers)

# numbers.sort() #по зростанню
# print(numbers)
# numbers.sort(reverse=True) #по спаданню
# print(numbers)
# print(sorted(numbers)) #не змінює сам список
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# for n in numbers:
#     print(n)

# digits = [2, 8, -9, 5, 7, 0, -4]
# dodatni = []
# parni = []
# for d in digits:
#     if d > 0:
#         dodatni.append(d)
#     if d % 2 == 0:
#         parni.append(d)
# print(dodatni)
# print(parni)





#tuple - кортеж(впорядкована НЕЗМІННА колекція)
# rgb = (255, 0, 0)
# r, g, b = rgb
# print(r, g, b)
#
# data = ()
# a = (1,)
# індексація як в ліст

# point = (4, -6)
# point = point + (4,) #додавання кортежів





#set - множина(послідовність унікальних елементів)
# subjects = {"Python", "HTML", "CSS", "JavaScript"}
# print(subjects)
# data = {}
# print(type(data))
# data2 = set()
# data2.add("Python")
# data2.update(["JavaScript", "CSS"])
# print(data2)
# data2.remove("JavaScript") #краще discard, щоб без помилки(але якщо 1 елемент)
# print(data2)
#
# name = ["ivan", "pipin korotki", "ivan", "kostyan", "yamete kudasai"]
# newnames = set(name)
# print(newnames)

# names1 = {"ivan", "ivan", "vkusnyashko"}
# names2 = {"kuku", "ivan", "sobaka"}
# names3 = names1 | names2 # об'єднання, тільки 1 раз всі
# names4 = names1 & names2 # перетин
# names5 = names1 - names2 # віднімання, ті що лиш в 1 після віднімання перетину





#dict - словники
# student = {
#     "name": "Olesia",
#     "age": 16,
# }

# prod = {"bread", "milk", "tomato"}
# price = {40, 35, 15}
# prices = {
#     "bread": 40,
#     "milk": 35,
#     "tomato": 15
# }
# print(prices["bread"])
# prices["tea"] = 90

# .get()
# .value()
# .key()
# .items()

# for key,value in prices.items():
#     print(key,value)
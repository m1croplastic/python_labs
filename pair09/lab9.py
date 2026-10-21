# 1
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def area(self):
#         return self.width * self.height
#     def info(self):
#         print(f"Розміри прямокутника: {self.width} x {self.height}")
#         print(f"S={self.area()}")
#         print(f"P={self.perimeter()}")
#
# a = int(input("Введіть ширину 1 прямокутника: "))
# b = int(input("Введіть довжину 1 прямокутника: "))
# c = int(input("Введіть ширину 2 прямокутника: "))
# d = int(input("Введіть довжину 2 прямокутника: "))
# rectangle1 = Rectangle(a, b)
# rectangle2 = Rectangle(c, d)
# rectangle1.info()
# rectangle2.info()



# 2
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self):
#         while True:
#             grade = int(input("Введіть оцінку 1-12(для виходу введіть 0): "))
#             if 1 <= grade <= 12:
#                self.grades.append(grade)
#             if grade == 0:
#                 break
#
#     def average(self):
#         if len(self.grades) > 0:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return 0
#
#     def __str__(self):
#         return f"{self.name}: {self.grades}, середній бал: {self.average()}"
#
# n = input("Введіть ім'я учня: ")
# student = Student(n, [])
# student.add_grade()
# print(student.__str__())



# 3
#
# class Student:
#      def __init__(self, name, grades):
#          self.name = name
#          self.grades = grades
#
#
#      def average(self):
#              return sum(self.grades) / len(self.grades)
#
# students = [
# Student("Аня", [10, 6, 12]),
# Student("Олеся", [8, 9, 10]),
# Student("Даша", [7, 12, 11]),
# Student("Ліза", [10, 10, 9]),
# Student("Мар'янкояйко", [10, 9, 9])
# ]
# for student in students:
#    print(student.name)
#    print(student.grades)
#
# best_student = students[0]
# for student in students:
#     if student.average() > best_student.average():
#        best_student = student
# print("Учень з найвищим сер. балом:", best_student.name, round(best_student.average(), 2))



# 4
#
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Сума поповнення має бути додатньою")
#         else:
#             self.balance += amount
#             print(f"+{amount}")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сума зняття має бути додатньою")
#         elif amount > self.balance:
#             print("Недостатньо грошей на рахунку")
#         else:
#             self.balance -= amount
#             print(f"-{amount}")
#
#     def __str__(self):
#         return f"{self.owner}: баланс {self.balance} грн."
#
# wallet1 = Wallet("Олеся", 2500)
# wallet2 = Wallet("Мар'янкояйко", 90500)
#
# print(wallet1.__str__())
# wallet1.deposit(100)
# wallet1.withdraw(2000)
# wallet1.withdraw(1000)
# print(wallet1.__str__())
#
# print(wallet2.__str__())
# wallet2.deposit(50)
# wallet2.withdraw(-3000)
# wallet2.withdraw(0)
# print(wallet2.__str__())
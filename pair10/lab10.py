# 1
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Тіпочок: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
#
# student1 = Student("Olesia", "10-IT(17)")
# student2 = Student("Nika", "10-IT(18)")
# print(student1.info())
# print(student2.info())



# 2
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Тіпочок: {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#     def info(self):
#         return f"Вчитель: {self.name}, предмет: {self.subject}"
#
# people = [Person("Artem"), Student("Liza", "10-IT(17)"),Student("Olesia", "10-IT(17)"), Teacher("Ivan", "IT")]
# for p in people:
#     print(p.info())



# 3
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
# class Course:
#     def __init__(self, title, teacher, students):
#         self.title = title
#         self.teacher = teacher
#         self.students = students
#
#     def add_student(self, student):
#         for s in self.students:
#             if s.name == student.name:
#                 print("Учень вже у списку")
#                 return
#         print("Учня додано")
#         self.students.append(student)
#
#     def remove_student(self, name):
#         for s in self.students:
#             if s.name == name:
#                 self.students.remove(s)
#                 print("Учня видалено")
#                 return
#         print("Такого учня немає")
#
#     def show_students(self):
#         print(f"Учні «{self.title}»:")
#         for s in self.students:
#             print(s.name, s.group)
#
# course = Course("10-IT", Teacher("Ivan", "IT"), [])
#
# course.add_student(Student("Olesia", "17"))
# course.add_student(Student("Liza", "17"))
# course.add_student(Student("Nika", "18"))
# course.add_student(Student("Liza", "17"))
# course.add_student(Student("Sonya", "18"))
#
# course.remove_student("Nika")
#
# course.show_students()



# 4
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Student(Person):
#     def __init__(self, name, group, grades):
#         super().__init__(name)
#         self.group = group
#         self.grades = grades
#
#     def add_grade(self, grade):
#         grade = int(input("Введіть оцінку учня: "))
#         if grade<1 or grade>12:
#             print("Неможлива оцінка")
#         self.grades.append(grade)
#
#     def average(self):
#         if len(self.grades)==0:
#             return 0
#         return sum(self.grades)/len(self.grades)
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
# class Course:
#     def __init__(self, title, teacher, students):
#         self.title = title
#         self.teacher = teacher
#         self.students = students
#
#     def add_student(self, student):
#         for s in self.students:
#             if s.name == student.name:
#                 print("Учень вже у списку")
#                 return
#         print("Учня додано")
#         self.students.append(student)
#
#     def remove_student(self, name):
#         for s in self.students:
#             if s.name == name:
#                 self.students.remove(s)
#                 print("Учня видалено")
#                 return
#         print("Такого учня немає")
#
#     def show_students(self):
#         print(f"Учні «{self.title}»:")
#         for s in self.students:
#             print(s.name, s.group)
#
#     def find_student(self, name):
#         for s in self.students:
#             if s.name.lower == name.lower():
#                 return s
#         return None
#
#     def add_grade_to_student(self, name, grade):
#         s = self.find_student(name)
#         if s:
#             s.add_grade = grade
#         else:
#             print("Такого учня немає")
#
#     def show_rating(self):
#         if len(self.students)==0:
#             print("Немає учнів")
#             return
#         rating = sorted(self.students, key=lambda s: s.average, reverse=True)
#         print("Рейтинг:")
#         for i, s in enumerate(rating):
#             print(f"{i}. {s.name}: {s.average}")
#
# course = Course("10-IT", Teacher("Ivan", "IT"), [])
#
# while True:
#     print("Меню:")
#     print("1 — Показати курс")
#     print("2 — Додати учня")
#     print("3 — Видалити учня")
#     print("4 — Знайти учня")
#     print("5 — Виставити оцінку")
#     print("6 — Показати рейтинг")
#     print("7 — Зберегти дані")
#     print("0 — Вихід")
#
#     choice = input("Ваш вибір: ")
#     if choice == "1":
#         course.show_students()
#
#     elif choice == "2":
#         name = input("Ім'я учня:")
#         group = input("Група учня: ")
#         course.add_student(Student(name, group, []))
#
#     elif choice == "3":
#         name = input("Ім'я учня для видалення: ")
#         course.remove_student(name)
#
#     elif choice == "4":
#         name = input("Ім'я учня для пошуку: ")
#         student = course.find_student(name)
#
#         if student:
#             print(f"Ім'я: {student.name}")
#             print(f"Група: {student.group}")
#             print(f"Оцінки: {student.grades}")
#             print(f"Середнє: {student.average}")
#
#         else:
#             print("Учня не знайдено")
#
#     elif choice == "5":
#         name = input("Ім'я учня: ")
#         grade = int(input("Оцінка від 1 до 12: "))
#         course.add_grade_to_student(name, grade)
#
#     elif choice == "6":
#         course.show_rating()
#
#     elif choice == "7":
#         print("Технічні роботи, наразі цей пункт недоступний. Спробуйте ще раз")
#
#     elif choice == "0":
#         break
#
#     else:
#         print("Неіснуючий пункт. Спробуйте ще раз")
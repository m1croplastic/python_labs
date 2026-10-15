# 1
#
# with open("text.txt", "r", encoding="utf-8") as file:
#      text = file.read()
# lines = text.split("\n")
# lines_c = len(lines)
# word_c = len(text.split())
# char_c = len(text)
# long = ""
# with open("text.txt", "r", encoding="utf-8") as file:
#     for number, line in enumerate(file, start=1):
#         for l in lines:
#             if len(l) > len(long):
#                 long = l
# print("Рядків:", lines_c)
# print("Слів:", word_c)
# print("Символів:", char_c)
# print("Довжина найдовшого рядка:", len(long))
# print(number, long)






# 2
#
# frg = input("Фрагмент: ").lower()
# ye = False
# with open("text.txt", "r", encoding="utf-8") as file:
#     for number, line in enumerate(file, start=1):
#         if frg in line.lower():
#             print(number, line)
#             ye = True
# if ye == False:
#     print("Немає збігів")







# 3
#
# students = []
# umni = []
# with open("students.txt", "r", encoding="utf-8") as file:
#      for line in file:
#          name, grade = line.strip().split(';')
#          students.append([name, grade])
#          if int(grade) > 80:
#             umni.append([grade, name])
# umni.sort(reverse=True)
# umni_1 = []
# for grade, name in umni:
#     umni_1.append([name, grade])
# with open("result.txt", "w", encoding="utf-8") as file:
#     for name, grade in umni_1:
#             file.write(name + ';' + grade + '\n')
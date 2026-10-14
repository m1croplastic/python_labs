import random

def generate_grades(count):
    grades = []
    if count > 0:
        for i in range(count):
            grades.append(random.randint(1, 12))
    return grades

def average_grade(grades):
    if len(grades) >= 1:
        average = sum(grades) / len(grades)
    return average

def get_level(average):
    if average < 4:
        return "початковий рівень"
    elif 4 <= average <= 6.99:
        return "середній рівень"
    elif 7 <= average <= 9.99:
        return "достатній рівень"
    else:
        return "високий рівень"
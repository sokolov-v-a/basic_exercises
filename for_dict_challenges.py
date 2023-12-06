# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

students_names = {}
for student in students:
    name = student['first_name']
    if name in students_names:
       students_names[name] += 1
    else:
        students_names[name] = 1  
for name in students_names:
    print(f"{name}: {students_names[name]}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
students_names = {}
for student in students:
    name = student['first_name']
    if name in students_names:
       students_names[name] += 1
    else:
        students_names[name] = 1  
students_names_sorted = sorted(students_names.items(), key=lambda x: x[1], reverse=True)

print(f"Самое частое имя среди учеников: {students_names_sorted[0][0]}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


class_number = 0
for students in school_students:
    class_number += 1
    students_names = {}
    for student in students:
        name = student['first_name']
        if name in students_names:
            students_names[name] += 1
        else:
            students_names[name] = 1  
    students_names_sorted = sorted(students_names.items(), key=lambda x: x[1], reverse=True)

    print(f"Самое частое имя в классе {class_number}: {students_names_sorted[0][0]}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_calass in school:
    male = {"девочки": 0, "мальчики": 0}
    for student in school_calass['students']:
        name = student['first_name']
        if is_male[name] == True:
            male['мальчики'] += 1
        elif is_male[name] == False:
            male['девочки'] += 1
    print(f"Класс {school_calass['class']}: девочки {male['девочки']}, мальчики {male['мальчики']} ")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

girls = {}
boys = {}

for school_calass in school:
    print(school_calass)
    for student in school_calass['students']:
        name = student['first_name']
        class_name = school_calass['class']
        if is_male[name] == True:
            if class_name in boys:
                boys[class_name]+= 1
            else:
                boys[class_name] = 1
        elif is_male[name] == False:
            if class_name in girls:
                girls[class_name]+= 1
            else:
                girls[class_name] = 1
sorted_girls = sorted(girls.items(), key= lambda x: x[1], reverse=True)
sorted_boys  = sorted(boys.items(),  key= lambda x: x[1], reverse=True)

print(f"Больше всего мальчиков в классе {sorted_boys[0][0]}: {sorted_boys[0][1]}")
print(f"Больше всего девочек в классе {sorted_girls[0][0]}: {sorted_girls[0][1]}")

# Добавляем файл functions
import functions
# Импортируем sys
import sys

# Спрашиваем имя студента
student_number = input("Введите номер студента")
# Загружаем список студентов из файла
students = functions.load_students()

# Получаем словарь с данными студента
found_student = functions.get_student_by_pk(students, int(student_number))

# Выводим информацию о пользователе
if found_student:
    print(f"Студент {found_student['full_name']}")
    print(f"Знает {', '.join(found_student['skills'])}")
    # Спрашиваем специальность для оценки студента
    student_profession = input(f"Выберите специальность для оценки студента {found_student['full_name']}").lower()
    # Запрашиваем список студентов из файла
    professions = functions.load_professions()

    # Получаем словарь с информацией о профессии
    found_profession = functions.get_profession_by_title(professions, student_profession)
    for profession in professions:
        if student_profession.lower() == profession["title"].lower():
            found_profession = profession
            break
    if found_profession:
        # Получаем профессию студента и выводим словарь
        fitness = functions.check_fitness(found_student['skills'], found_profession['skills'])
        print(f"Пригодность {fitness['fit_percent']}%")
        print(f"{found_student['full_name']} знает {','.join(fitness['has'])}")
        print(f"{found_student['full_name']} не знает {','.join(fitness['lacks'])}")
    else:
        print("У нас нет такой специальности")
else:
    print("У нас нет такого студента")
    sys.exit(1)

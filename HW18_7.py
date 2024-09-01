import random
        # список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
        # отсортируем список учеников
students.sort()
        # список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
        # пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
        # сгенерируем данные по оценкам:
        # цикл по ученикам
for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
            # цикл по предметам
    for class_ in classes: # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
        {students_marks[student]}''')
        
        
    print('''
    Список команд:
    1. Добавить оценки ученика по предмету
    2. Вывести средний балл по всем предметам по каждому ученику
    3. Вывести все оценки по всем ученикам
    4. Удаление оценки ученика по предмету
    5. Редактирование оценки ученика по предмету
    6. Удаление данных о предмете
    7. Редактирование данных о предмете
    8. Удаление данных об ученике
    9. Редактирование данных об ученике
    10. Вывод всех оценок определенного ученика
    11. Вывод среднего балла для определенного ученика по каждому предмету
    12. Показать аттестованны ли ученики по выбранному предмету
    13. Выход из программы
    ''')
    #неаттестованными считаются те ученики у которых средний балл меньше 2, ученик является аттестованным если его средний балл больше или равен 3
    while True:
        command = int(input('Введите команду: '))
        if command == 1:
            print('1. Добавить оценку ученика по предмету')
            # считываем имя ученика
            student = input('Введите имя ученика: ')
            # считываем название предмета
            class_ = input('Введите предмет: ')
            # считываем оценку
            mark = int(input('Введите оценку: '))
            # если данные введены верно
            if student in students_marks.keys() and class_ in students_marks[student].keys() and mark >=1 and mark <= 5:
                # добавляем новую оценку для ученика по предмету
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
            # неверно введены название предмета или имя ученика
            else:
                print('ОШИБКА: неверное имя ученика, название предметаили некорректное значение оценки')
        elif command == 2:
            print('2. Вывести средний балл по всем предметам по каждому ученику')
            # цикл по ученикам
            for student in students:
                print(student)
                # цикл по предметам
                for class_ in classes:
                    # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[student][class_])
                    # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                    # выводим средний балл по предмету
                    print(f'{class_} - {marks_sum//marks_count}')
                print()
        elif command == 3:
            print('3. Вывести все оценки по всем ученикам')
            # выводим словарь с оценками:
            # цикл по ученикам
            for student in students:
                print(student)
                # цикл по предметам
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        elif command == 4:
            print('4. Удаление оценки ученика по предмету')
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            index = int(input('Введите номер оценки, которую вы хотите удалить:'))
            if student in students_marks.keys() and class_ in students_marks[student].keys() and index <= len(students_marks[student][class_])+1:
                # добавляем новую оценку для ученика по предмету
                students_marks[student][class_].pop(index-1)
                print(f'Для {student} по предмету {class_} удалена оценка под номером {index}')
            # неверно введены название предмета или имя ученика
            else:
                print('ОШИБКА: неверное имя ученика, название предмета или номер оценки')
        elif command == 5:
            print('5. Редактирование оценки ученика по предмету: ')
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            index = int(input('Введите номер оценки, которую вы хотите редактировать:'))
            mark = int(input('Введите оценку которую вы ходите добавить вместо находящейся на выбранном вами месте:'))
            if student in students_marks.keys() and class_ in students_marks[student].keys() and index <= len(students_marks[student][class_])+1 and mark >=1 and mark <= 5:
                students_marks[student][class_][index-1] = mark
                print(f'Для {student} по предмету {class_} оценка под номером {index} измененна на {mark}')
            else:
                print('ОШИБКА: неверное имя ученика, название предмета, номер оценки или некорректное значение оценки')
        elif command == 6:
            print('6. Удаление данных о предмете:')
            class_ = input('Введите название предмета данные о котором вы хотите удалить:')
            if class_ in classes:
                classes.remove(class_)
                for c in students_marks:
                    students_marks[c].pop(class_)
                print(f'Данные о предмете {class_} удалены')
            else:
                print('ОШИБКА: неверное название предмета')
        elif command == 7:
            print('7. Редактирование данных о предмете:')
            class_ = input('Введите название предмета информацию о котором вы хотите редактировать')
            class_mod = input('Введите новое название предмета информацию о котором вы хотите редактировать')
            if class_ in classes:
                classes.append(class_mod)
                classes.remove(class_)
                for c in students_marks:
                    students_marks[c][class_mod] = students_marks[c][class_]
                    students_marks[c].pop(class_)
                print(f'Данные о предмете {class_} измененны на {class_mod} и добавленны в конец списка предметов')
            else:
                print('ОШИБКА: неверное название предмета')
        elif command == 8:
            print('8. Удаление данных об ученике:')        
            student = input('Введите имя ученика данные о котором вы хотите удалить')
            if student in students:
                students.remove(student)
                students_marks.pop(student)
                print(f'Данные об ученике {student} удалены')
            else:
                print('ОШИБКА: введено некорректное имя ученика')
        elif command == 9:
            print('9. Редактирование данных об ученике:')
            student = input('Введите имя ученика информацию о котором вы хотите отредактировать')
            student_mod = input('Введите новое имя выбранного ранее ученика')
            if student in students:
                students.remove(student)
                students.append(student_mod)
                students_marks[student_mod] = students_marks[student]
                students_marks.pop(student)
                print(f'Данные об ученике {student} измененны на {student_mod} и добавленны в конец списка учеников')
            else:
                print('ОШИБКА: введено некорректное имя ученика')
        elif command == 10:
            print('Вывод всех оценок определенного ученика:')
            student = input('Введите имя ученика оценки которого вы хотели бы увидеть')
            if student in students:
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
            else:
                print('ОШИБКА: некорректное имя ученика')
        elif command == 11:
            print('Вывод среднего балла для определенного ученика по каждому предмету')
            student = input('Введите имя ученика средний балл которого вы хотели бы увидеть')
            if student in students:
                for class_ in classes:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum//marks_count}')
            else:
                print('ОШИБКА: введено некорректное имя ученика')
        elif command == 12:
            print('12. Показать аттестованны ли ученики по выбранному предмету')
            class_ = input('Введите название предмета информацию о котором вы хотите получить')
            if class_ in classes:
                for student in students:
                    marks_sum = sum(students_marks[student][class_])
                    # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                    if (marks_sum//marks_count) > 2:
                        print(f'{student} - аттестован')
                    else:
                        k = 0
                        while (marks_sum//marks_count) <= 2:
                            marks_sum+=5
                            marks_count+=1
                            k+=1
                        print(f'{student} - неаттестован, для аттестации по выбранному предмету нужно получить {k} пятерок')
        elif command == 13:
            print('12. Выход из программы')
            break
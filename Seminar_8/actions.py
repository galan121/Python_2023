import log
import user_interface as ui
import controller
import rw_mod as db
from tabulate import tabulate

def searching():
    ui.show_search_menu()
    db.read_file()
    n =input('Пожалуйста, введите цифру, соответствующую пункту меню: ')
    if n == '1':
        search = input('Пожалуйста, введите id студента: ')
        print(tabulate(students_info(id=search)))
    elif n == '2':
        search = input('Пожалуйста, введите фамилию студента: ')
        print(tabulate(students_info(surname=search)))
    elif n == '3':
        search = input('Пожалуйста, введите наименование курса: ')
        print(tabulate(students_info(course=search)))
    elif n == '4':
        search = input('Пожалуйста, введите фамилию преподавателя: ')
        print(tabulate(students_info(mentor=search)))
    elif n == '5':
        search = input('Пожалуйста, введите группу: ')
        print(tabulate(students_info(group=search)))
    elif n == '6':
        log.logging.info('returned to previous menu')
        print('Возврат в предыдущее меню')
        controller.main_menu()
    elif n == '7':
        log.logging.info('Stop program')
        ui.show_exit_message()
        exit()
    else:
        ui.show_error_menu()
        controller.main_menu()


def students_info(id='', surname='', course='', group='', mentor=''):
    result = []
    for row in db.db_book:
        if (id != '' and row[0] != id):
            continue
        if (surname != '' and row[1] != surname.title()):
            continue
        if (course != '' and row[7] != course.title()):
            continue
        if (group != '' and row[8] != group):
            continue
        if (mentor != '' and row[9] != mentor.title()):
            continue
        result.append(row)
    if len(result) == 0:
        return print("Студенты не найдены")
    else:
        return result

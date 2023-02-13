import os.path
import log
import user_interface as ui
import csv

db_file = 'database.csv'
db_book = []
last_id = 0
blank_list = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Email', 'Дата рождения', 'Курс', 'Группа',
              'Преподаватель']


def read_file():
    global db_book, db_file, last_id, blank_list
    while True:
        if os.path.exists(db_file):
            with open(db_file, mode='r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file)
                db_book = [line for line in reader]
            last_id = int(db_book[-1][0])
            return db_book
        else:
            log.logging.error('Incorrect file')
            ui.show_error_file()
            ask_user = input('Хотите создать новую базу данных (y/n): ')
            if ask_user.lower() == 'y':
                with open(db_file, mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(blank_list)
                log.logging.info('New datafile was created')
                id_num = last_id + 1
                first_name = input('Введите фамилию: ')
                last_name = input('Введите имя: ')
                middle_name = input('Введите отчество: ')
                tel = input('Введите номер телефона: ')
                email = input('Введите Email: ')
                day_of_birth = input('Введите дату рождения: ')
                course = input('Введите курс: ')
                group = input('Введите группу: ')
                teacher = input('Введите данные преподавателя: ')
                new_person = [str(id_num), first_name, last_name, middle_name, tel, email, day_of_birth, course, group,
                              teacher]
                add_data(new_person)
                print('Данные успешно добавлены!')
                input('Для продолжения нажмите кнопку ввода...')
                break
            elif ask_user.lower() == 'n':
                ui.show_exit_message()
                exit()
            else:
                log.logging.error('Incorrect selection')
                ui.show_error_menu()


def write_file(new_db):
    with open(db_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for line in new_db:
            writer.writerow(line)
    log.logging.info('New datafile was created')


def add_data(new_data):
    with open(db_file, mode='a', encoding='utf-8', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    log.logging.info('New data was written')
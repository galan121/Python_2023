import log
import rw_mod as db
import user_interface as ui


def create_data():
    db.read_file()
    id_num = db.last_id + 1
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    tel = input('Введите номер телефона: ')
    email = input('Введите Email: ')
    day_of_birth = input('Введите дату рождения: ')
    course = input('Введите курс: ')
    group = input('Введите группу: ')
    teacher = input('Введите данные преподавателя: ')
    new_person = [str(id_num), first_name, last_name, middle_name, tel, email, day_of_birth, course, group, teacher]
    db.add_data(new_person)
    print('Данные успешно добавлены!')
    input('Для продолжения нажмите кнопку ввода...')


def find_data(num_id):
    db.read_file()
    index_id = 0
    for i in range(1, len(db.db_book)):
        if db.db_book[i][0] == num_id: index_id = i
    return index_id


def change_data():
    id_num = input('Ввeдите id записи, которую необходимо изменить: ')
    ch_id_ind = find_data(id_num)
    if ch_id_ind == 0:
        print('Запись с таким id отсутствует в базе.')
    else:
        print('Запись найдена')
        print(*db.db_book[ch_id_ind], sep='\t')
        ask_user = input("Подтвердите необходимость ее изменения (y/n): ")
        if ask_user.lower() == 'y':
            f_name = input('Введите фамилию: ')
            l_name = input('Введите имя: ')
            m_name = input('Введите отчество: ')
            tel = input('Введите номер телефона: ')
            email = input('Введите Email: ')
            birth_d = input('Введите дату рождения: ')
            course = input('Введите курс: ')
            group = input('Введите группу: ')
            teacher = input('Введите данные преподавателя: ')
            db.db_book[ch_id_ind] = [str(id_num), f_name, l_name, m_name, tel, email, birth_d, course, group, teacher]
            db.write_file(db.db_book)
            log.logging.info('Database was changed')
            print(f'Данные id {id_num} успешно изменены!')
            input('Для продолжения нажмите кнопку ввода...')
        elif ask_user.lower() == 'n':
            print(f'Данные id {id_num} не были изменены!')
            input('Для продолжения нажмите кнопку ввода...')
        else:
            log.logging.error('Incorrect selection')
            ui.show_error_menu()


def del_data():
    id_num = input('Ввeдите id записи, которую необходимо удалить: ')
    del_id_index = find_data(id_num)
    if del_id_index == 0:
        print('Запись с таким id отсутствует в базе.')
    else:
        print('Запись найдена')
        print(*db.db_book[del_id_index], sep='\t')
        ask_user = input("Подтвердите удаление (y/n): ")
        if ask_user.lower() == 'y':
            db.db_book[del_id_index] = [str(id_num), '', '', '', '', '', '', '', '', '']
            db.write_file(db.db_book)
            print(f'Данные id {id_num} успешно удалены!')
            log.logging.info('Database was changed')
            input('Для продолжения нажмите кнопку ввода...')
        elif ask_user.lower() == 'n':
            print(f'Данные id {id_num} не были удалены!')
            input('Для продолжения нажмите кнопку ввода...')
        else:
            log.logging.error('Incorrect selection')
            ui.show_error_menu()

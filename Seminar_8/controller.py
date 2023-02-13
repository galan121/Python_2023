import log
import user_interface as ui
import actions as act
import rw_mod as db
import change_db
from tabulate import tabulate


def main_menu():
    while True:
        ui.show_main_menu()
        user_command = input('Пожалуйста, введите цифру, соответствующую пункту меню: ')
        if user_command == '0':
            log.logging.info('Stop program')
            ui.show_exit_message()
            exit()
        elif user_command == '1':
            log.logging.info('Show all data')
            print(tabulate(db.read_file()))
            input('Для продолжения нажмите кнопку ввода...')
        elif user_command == '2':
            log.logging.error('Selected searching block')
            act.searching()
        elif user_command == '3':
            log.logging.info('Enter new data')
            change_db.create_data()
        elif user_command == '4':
            change_db.change_data()
        elif user_command == '5':
            change_db.del_data()
        elif user_command not in ['0', '1', '2', '3', '4', '5']:
            log.logging.error('Incorrect selection')
            ui.show_error_menu()
            continue
        else:
            break

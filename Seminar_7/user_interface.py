import log
import calc_operations

def select_num_type():
    while True:
        type_num = input("\n"
                         "*****************************\n"
                         "* Types of numbers:         *\n"
                         "*****************************\n"
                         "* 1 - rational numbers      *\n"
                         "* 2 - complex numbers       *\n"
                         "* 0 - EXIT                  *\n"
                         "*****************************\n"
                         "Your selection: ")
        if type_num == '0':
            log.logging.info("Stop program")
            exit()
        elif type_num == '1':
            operation_for_rational_numbers()
        elif type_num == '2':
            operation_for_complex_number()
        elif type_num not in ['1', '2', '0']:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            continue
        else:
            break

def operation_for_rational_numbers():
    while True:
        oper = input("\n"
                               "*************************************************************\n"
                               "* Types of operation:                                       *\n"
                               "*************************************************************\n"
                               "* 1 - sum                                                   *\n"
                               "* 2 - subtraction                                           *\n"
                               "* 3 - multiplication                                        *\n"
                               "* 4 - division                                              *\n"
                               "* 5 - exponentiation                                        *\n"
                               "* 6 - root of first number (second number - degree of root) *\n"
                               "* 7 - remainder of division                                 *\n"
                               "* 8 - integer division                                      *\n"
                               "* 0 - previous menu                                         *\n"
                               "* 00 - EXIT                                                 *\n"
                               "*************************************************************\n"
                               "Your selection: ")
        if oper not in ['1', '2', '3', '4', '5', '6', '7', '8', '0', '00']:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            continue
        elif oper == '00':
            log.logging.info("Stop program")
            exit()
        elif oper == '0':
            log.logging.info('go to previous menu')
            break
        else:
            n1, n2 = rational_num(oper)
            calc_operations.actions(oper, n1, n2)
            log.logging.info('finish program')
            exit()

def operation_for_complex_number():
    while True:
        oper = input("\n"
                       "*************************************************************\n"
                       "* Types of operation:                                       *\n"
                       "*************************************************************\n"
                       "* 1 - sum                                                   *\n"
                       "* 2 - subtraction                                           *\n"
                       "* 3 - multiplication                                        *\n"
                       "* 4 - division                                              *\n"
                       "* 5 - exponentiation                                        *\n"
                       "* 6 - root of first number (second number - degree of root) *\n"
                       "* 0 - previous menu                                         *\n"
                       "* 00 - EXIT                                                 *\n"
                       "*************************************************************\n"
                       "Your selection: ")
        if oper not in ['1', '2', '3', '4', '5', '6', '0', '00']:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            continue
        elif oper == '00':
            log.logging.info("Stop program")
            exit()
        elif oper == '0':
            log.logging.info('go to previous menu')
            break
        else:
            if oper == '6': oper = '60'
            n1, n2 = complex_num(oper)
            calc_operations.actions(oper, n1, n2)
            log.logging.info('finish program')
            exit()

def rational_num(op):
    while True:
        try:
            num_1 = float(input("Enter 1 number: ").replace(',', '.'))
            num_2 = float(input("Enter 2 number: ").replace(',', '.'))
            return num_1, num_2
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            return

def complex_num(op):
    while True:
        if op == '60' or op == '5':
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = float(input("Enter 2 number: ").replace(',', '.'))
                num_C_1 = complex(num_1, num_2)
                return num_C_1, num_3
            except:
                log.logging.error("Error")
                print("Error. Incorrect input.")
                return
        else:
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = int(input("Enter 2 real part: "))
                num_4 = int(input("Enter 2 imaginary number: "))
                num_C_1 = complex(num_1, num_2)
                num_C_2 = complex(num_3, num_4)
                return num_C_1, num_C_2
            except:
                log.logging.error("Error")
                print("Error. Incorrect input.")
                return
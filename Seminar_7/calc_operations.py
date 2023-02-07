import user_interface as mod
import log


def actions(act_operation, num_1, num_2):
    if act_operation == '1':
        log.logging.info(f'{num_1} + {num_2} = {num_1 + num_2}')
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    elif act_operation == '2':
        log.logging.info(f'{num_1} - {num_2} = {num_1 - num_2}')
        print(f'{num_1} - {num_2} = {num_1 - num_2}')
    elif act_operation == '3':
        log.logging.info(f'{num_1} * {num_2} = {num_1 * num_2}')
        print(f'{num_1} * {num_2} = {num_1 * num_2}')
    elif act_operation == '4':
        if num_2 == 0:
            log.logging.error("Error")
            print("Error. It cannot be divided by 0.")
            exit()
        else:
            log.logging.info(f'{num_1} / {num_2} = {num_1 / num_2}')
            print(f'{num_1} / {num_2} = {num_1 / num_2}')
    elif act_operation == '5':
            log.logging.info(f'{num_1} ** {num_2} = {num_1 ** num_2}')
            print(f'{num_1}^{num_2} = {num_1 ** num_2}')
    elif act_operation == '6':
        if num_2 == 0:
            log.logging.error("Error")
            print("Error. Invalid argument.")
            exit()
        elif num_2 % 2 == 0 and num_1 < 0:
            log.logging.error("Error")
            print("Error. Invalid argument.")
            exit()
        else:
            log.logging.info(f'{num_1} root {num_2} = {num_1 ** (1/num_2)}')
            print(f'The root of degree {num_2} of {num_1} is {num_1 ** (1/num_2)}')
    elif act_operation == '60':
        if num_2 == 0:
            log.logging.error("Error")
            print("Error. Invalid argument.")
            exit()
        else:
            log.logging.info(f'{num_1} root {num_2} = {num_1 ** (1/num_2)}')
            print(f'The root of degree {num_2} of {num_1} is {num_1 ** (1/num_2)}')
    elif act_operation == '7':
        if num_2 == 0:
            log.logging.error("Error")
            print("Error. It cannot be divided by 0.")
            exit()
        else:
            log.logging.info(f'{num_1} % {num_2} = {num_1 % num_2}')
            print(f'The remainder of dividing {num_1} by {num_2} is {num_1 % num_2}')
    elif act_operation == '8':
        if num_2 == 0:
            log.logging.error("Error")
            print("Error. It cannot be divided by 0.")
            exit()
        else:
            log.logging.info(f'{num_1} // {num_2} = {num_1 // num_2}')
            print(f'Result of integer division {num_1} by {num_2} is {num_1 // num_2}')
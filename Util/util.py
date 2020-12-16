import re
log_level = 1


def remove(my_list):
    pattern = '[0-9]'
    my_list = [re.sub(pattern, '', i) for i in my_list]
    return my_list


def print_debug(message, debug_on=1):
    if debug_on == 1:
        if log_level >= 1:
            print(message)

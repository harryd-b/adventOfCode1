import re

debug_on = 1


def remove(my_list):
    pattern = '[0-9]'
    my_list = [re.sub(pattern, '', i) for i in my_list]
    return my_list


def print_debug(message):
    if debug_on == 1:
        print(message)

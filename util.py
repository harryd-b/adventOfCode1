import re


def remove(my_list):
    pattern = '[0-9]'
    my_list = [re.sub(pattern, '', i) for i in my_list]
    return my_list

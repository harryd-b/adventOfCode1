from Util.file import load_file_to_list
from Day4.ppt import Passport


def populate_from_raw(raw_passports, passport_list):

    passport_counter = 0

    # create our first passport object
    # loop through each line
    for i in range(len(raw_passports)):
        line = raw_passports[i]
        # have we reached a new passport?
        if line == "":
            passport_counter += 1
            passport_list.append(Passport())
            continue
        my_passport = passport_list[passport_counter]
        pairs = line.split(" ")
        for j in range(len(pairs)):
            my_pair = pairs[j].split(":")
            setattr(my_passport, my_pair[0], my_pair[1])
    return passport_list

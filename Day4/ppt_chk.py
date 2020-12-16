from Util.file import load_file_to_list
from Day4.ppt import Passport


def populate_from_raw(passport_map):

    passport_counter = 0
    passport_list = [Passport()]
    # create our first passport object
    # loop through each line
    for i in range(len(passport_map)):
        line = passport_map[i]
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

    valid_passport_counter = 0
    for k in range(len(passport_list)):
        if passport_list[k].is_passport_valid():
            valid_passport_counter += 1

    print(str(valid_passport_counter))


if __name__ == '__main__':
    populate_from_raw()

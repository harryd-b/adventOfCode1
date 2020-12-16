from Util.file import load_file_to_list


def get_row(key):
    first_letter = key[0]
    start_num = 0
    end_num = 127
    row = 0
    for i in range(len(key) - 3):
        if key[i] == "F":
            end_num = end_num - (((end_num + 1) - start_num) / 2)
            if i == 6:
                row = end_num
        elif key[i] == "B":
            start_num = start_num + (((end_num + 1) - start_num) / 2)
            if i == 6:
                row = start_num

    return int(row)


def get_column(key):
    start_num = 0
    end_num = 7
    column = 0
    for i in range(7, 10):

        if key[i] == "L":
            end_num = end_num - (((end_num + 1) - start_num) / 2)
            if i == 9:
                column = end_num
        elif key[i] == "R":
            start_num = start_num + (((end_num + 1) - start_num) / 2)
            if i == 9:
                column = start_num
    return int(column)
    return 0


def load_loop():
    pass_map = []
    load_file_to_list('../venv/Include/pass.txt', pass_map)
    rows = []
    columns = []
    seats = []
    for i in range(len(pass_map)):
        my_row = get_row(pass_map[i])
        my_column = get_column(pass_map[i])
        rows.append(my_row)
        columns.append(my_column)
        my_seat = my_row * 8 + my_column
        seats.append(my_seat)

    sorted_seats = sorted(seats, reverse=True)

    for i in range(1, len(sorted_seats)):
        print(sorted_seats[i])

        if (sorted_seats[i] - sorted_seats[i - 1]) < -1:
            print(sorted_seats[i])


if __name__ == '__main__':
    load_loop()

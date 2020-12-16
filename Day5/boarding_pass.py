

class BoardingPass:

    @staticmethod
    def get_row(key):
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

    @staticmethod
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

    @staticmethod
    def get_sorted_seats(boarding_passes):
        rows = []
        columns = []
        seats = []
        for i in range(len(boarding_passes)):
            my_row = BoardingPass.get_row(boarding_passes[i])
            my_column = BoardingPass.get_column(boarding_passes[i])
            rows.append(my_row)
            columns.append(my_column)
            my_seat = my_row * 8 + my_column
            seats.append(my_seat)
        return sorted(seats, reverse=True)

    @staticmethod
    def get_missing_seat(sorted_seats):
        missing_seat = 0
        for i in range(1, len(sorted_seats)):
            if (sorted_seats[i] - sorted_seats[i - 1]) < -1:
                missing_seat = sorted_seats[i] + 1
        return missing_seat

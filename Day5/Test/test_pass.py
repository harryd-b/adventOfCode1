from unittest import TestCase
from Util.file import load_file_to_list
from Util.util import print_debug
from Day5.boarding_pass import BoardingPass


class TestBoardingPass(TestCase):
    def test_get_sorted_seats(self):
        boarding_passes = []
        load_file_to_list('../Resources/Day5.txt', boarding_passes)
        sorted_seats = BoardingPass.get_sorted_seats(boarding_passes)
        print_debug("***********************************", 1)
        print_debug("Day5 - Binary Boarding: Part1 ", 1)
        print_debug("The highest seat is: ")
        print_debug(str(sorted_seats[0]))

    def test_get_missing_seat(self):
        boarding_passes = []
        load_file_to_list('../Resources/Day5.txt', boarding_passes)
        sorted_seats = BoardingPass.get_sorted_seats(boarding_passes)
        print_debug("***********************************", 1)
        print_debug("Day5 - Binary Boarding: Part2 ", 1)
        print_debug("The missing seat is: ")
        print_debug(str(BoardingPass.get_missing_seat(sorted_seats)))

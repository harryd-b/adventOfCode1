from unittest import TestCase
from Day1.sums import Sums
from Util.file import load_file_to_list
from Util.util import print_debug


class TestSums(TestCase):
    DEBUG_ON = 1

    def test_part1(self):
        expense_list = []
        my_sum = Sums()
        print_debug("Loading Day 1 data", self.DEBUG_ON)
        load_file_to_list('../Resources/Day1.txt', expense_list)
        print_debug("Day 1 Part 1: Running find_sum for target: 2020 and combination of 2 numbers", self.DEBUG_ON)
        return_list = my_sum.find_sum(2020, list(map(int, expense_list)), 2)
        print_debug(return_list, self.DEBUG_ON)
        self.assertEqual(return_list[0], 1882)
        self.assertEqual(return_list[1], 138)
        self.assertEqual(return_list[2], 259716)

    def test_part2(self):
        expense_list = []
        my_sum = Sums()
        print_debug("Loading Day 1 data", self.DEBUG_ON)
        load_file_to_list('../Resources/Day1.txt', expense_list)
        print_debug("Day 1 Part 2: Running find_sum for target: 2020 and combination of 3 numbers", self.DEBUG_ON)
        return_list = my_sum.find_sum(2020, list(map(int, expense_list)), 3)
        print_debug(return_list, self.DEBUG_ON)
        self.assertEqual(return_list[0], 272)
        self.assertEqual(return_list[1], 308)
        self.assertEqual(return_list[2], 1440)
        self.assertEqual(return_list[3], 120637440)

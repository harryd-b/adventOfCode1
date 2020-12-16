import unittest
from Day1.sums import find_sum
from Util.file import load_file_to_list
from Util.util import print_debug


class MyTestCase(unittest.TestCase):
    def test_part1(self):
        expense_list = []
        print_debug("Loading Day 1 data")
        load_file_to_list('../venv/Include/Day1.txt', expense_list)
        print_debug("Day 1 Part 1: Running find_sum for target: 2020 and combination of 2 numbers")
        return_list = find_sum(2020, list(map(int, expense_list)), 2)
        print_debug(return_list)
        self.assertEqual(return_list[0], 1882)
        self.assertEqual(return_list[1], 138)
        self.assertEqual(return_list[2], 259716)

    def test_part2(self):
        expense_list = []
        print_debug("Loading Day 1 data")
        load_file_to_list('../venv/Include/Day1.txt', expense_list)
        print_debug("Day 1 Part 2: Running find_sum for target: 2020 and combination of 3 numbers")
        return_list = find_sum(2020, list(map(int, expense_list)), 3)
        print_debug(return_list)
        self.assertEqual(return_list[0], 272)
        self.assertEqual(return_list[1], 308)
        self.assertEqual(return_list[2], 1440)
        self.assertEqual(return_list[3], 120637440)

import unittest
from Util.file import load_file_to_list
from Day2.pwds import check_all
from Util.util import print_debug


class MyTestCase(unittest.TestCase):

    def test_passwords_part_1(self):
        passwords_list = []
        load_file_to_list('../venv/Include/Day2.txt', passwords_list)
        part_1 = check_all(passwords_list, 1)
        print_debug("Day 2 - Part 1:")
        print_debug(part_1)
        self.assertEqual(part_1, 477)

    def test_passwords_part_2(self):
        passwords_list = []
        load_file_to_list('../venv/Include/Day2.txt', passwords_list)
        part_2 = check_all(passwords_list, 2)
        print_debug("Day 2 - Part 2:")
        print_debug(part_2)

        self.assertEqual(part_2, 686)


if __name__ == '__main__':
    unittest.main()

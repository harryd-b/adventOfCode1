from unittest import TestCase
from Util.util import print_debug
from Day2.passwords import Passwords
from Util.file import load_file_to_list


class TestPasswords(TestCase):
    DEBUG_ON = 1

    def test_check_all(self):
        passwords_list = []
        load_file_to_list('../Resources/Day2.txt', passwords_list)
        part_1 = Passwords.check_all(passwords_list, self.DEBUG_ON)
        print_debug("Day 2 - Part 1:", self.DEBUG_ON)
        print_debug(part_1, self.DEBUG_ON)
        self.assertEqual(part_1, 477)

    def test_check_all_1(self):
        passwords_list = []
        load_file_to_list('../Resources/Day2.txt', passwords_list)
        part_2 = Passwords.check_all(passwords_list, 2)
        print_debug("Day 2 - Part 2:", self.DEBUG_ON)
        print_debug(part_2, self.DEBUG_ON)
        self.assertEqual(part_2, 686)

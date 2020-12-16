from unittest import TestCase
from Util.util import print_debug
from Day2.passwords import Passwords
from Util.file import load_file_to_list


class TestPasswords(TestCase):
    def test_check_pwd(self):
        self.fail()

    def test_check_pwd_1(self):
        self.fail()

    def test_split_data(self):
        self.fail()

    def test_check_all(self):
        self.fail()

    def test_passwords_part_1(self):
        passwords_list = []
        load_file_to_list('../venv/Include/Day2.txt', passwords_list)
        my_passwords = Passwords
        part_1 = my_passwords.check_all(passwords_list, 1)
        print_debug("Day 2 - Part 1:")
        print_debug(part_1)
        self.assertEqual(part_1, 477)

    def test_passwords_part_2(self):
        passwords_list = []
        load_file_to_list('../venv/Include/Day2.txt', passwords_list)
        my_passwords = Passwords
        part_2 = my_passwords.check_all(passwords_list, 2)
        print_debug("Day 2 - Part 2:")
        print_debug(part_2)

        self.assertEqual(part_2, 686)

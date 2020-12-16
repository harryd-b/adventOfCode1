import unittest
from Util.file import load_file_to_list
from Util.util import print_debug
from Day4.ppt import Passport
from Day4.ppt_chk import populate_from_raw


class MyTestCase(unittest.TestCase):

    def test_valid_passports_1(self):
        raw_passports = []
        passport_list = [Passport()]
        load_file_to_list('../venv/Include/Day4.txt', raw_passports)
        valid_passport_counter = 0
        populate_from_raw(raw_passports, passport_list)
        for k in range(len(passport_list)):
            if passport_list[k].is_passport_valid_1():
                valid_passport_counter += 1
        print_debug("")
        print_debug("***********************************")
        print_debug("Day4 - Passport Processing: Part2 ")
        print_debug("The counts of valid passports is: ")
        print_debug(str(valid_passport_counter))
        self.assertEqual(valid_passport_counter, 256)

    def test_valid_passports_2(self):
        raw_passports = []
        passport_list = [Passport()]
        load_file_to_list('../venv/Include/Day4.txt', raw_passports)
        valid_passport_counter = 0
        populate_from_raw(raw_passports, passport_list)
        for k in range(len(passport_list)):
            if passport_list[k].is_passport_valid_2():
                valid_passport_counter += 1
        print_debug("")
        print_debug("***********************************")
        print_debug("Day4 - Passport Processing: Part1 ")
        print_debug("The counts of valid passports is: ")
        print_debug(str(valid_passport_counter))
        self.assertEqual(valid_passport_counter, 198)
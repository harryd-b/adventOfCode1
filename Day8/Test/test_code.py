from unittest import TestCase
from Day8.code import Boot
from Util.file import load_file_to_list
from Util.util import print_debug


class TestBoot(TestCase):
    DEBUG_ON = 1

    def test_boot(self):
        instruction_list = []
        path = '../Resources/Day8.txt'
        load_file_to_list(path, instruction_list)
        my_boot = Boot
        my_boot.boot(my_boot, instruction_list)
        print_debug("***********************************", self.DEBUG_ON)
        print_debug("Day8 - Handheld Halting: Part1 ", self.DEBUG_ON)
        print_debug("The value of the accumulator is: ", self.DEBUG_ON)
        accumulator = my_boot.get_accumulator(my_boot)
        print_debug(accumulator, self.DEBUG_ON)
        self.assertTrue(accumulator, 1654)

    def test_boot_bug_finder(self):
        instruction_list = []
        path = '../Resources/Day8.txt'
        load_file_to_list(path, instruction_list)
        my_boot = Boot
        bug_line = my_boot.boot_bug_finder(my_boot, instruction_list)
        print_debug("***********************************", self.DEBUG_ON)
        print_debug("Day8 - Handheld Halting: Part2 ", self.DEBUG_ON)
        print_debug("The bug is on line: ", self.DEBUG_ON)
        print_debug(bug_line, self.DEBUG_ON)
        self.assertTrue(bug_line, 224)

    def test_fix_and_boot(self):
        instruction_list = []
        path = '../Resources/Day8.txt'
        load_file_to_list(path, instruction_list)
        my_boot = Boot
        bug_line = my_boot.boot_bug_finder(my_boot, instruction_list)
        bug_line -= 1
        my_boot.fix_bug(my_boot, instruction_list, bug_line)
        my_boot.boot(my_boot, instruction_list)
        print_debug("***********************************", self.DEBUG_ON)
        print_debug("Day8 - Handheld Halting: Part2 ", self.DEBUG_ON)
        print_debug("The value of the accumulator once the bug is fixed is: ", self.DEBUG_ON)
        accumulator = my_boot.get_accumulator(my_boot)
        print_debug(accumulator, self.DEBUG_ON)
        self.assertTrue(accumulator, 833)

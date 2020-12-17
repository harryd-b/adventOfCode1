from unittest import TestCase
from Util.file import load_file_to_list
from Util.util import print_debug
from Day6.forms import Forms


class TestForms(TestCase):
    def test_get_unanimous(self):
        form_list = []
        my_form = Forms
        load_file_to_list('../Resources/Day6.txt', form_list)
        my_form.get_groups(my_form, form_list)
        print_debug("***********************************", 1)
        print_debug("Day6 - Custom Customs: Part1 ", 1)
        print_debug("The count of answers is: ")
        print_debug(str(my_form.get_yes_counts(my_form, False)), 1)

    def test_get_counts(self):
        form_list = []
        my_form = Forms
        load_file_to_list('../Resources/Day6.txt', form_list)
        my_form.get_groups(my_form, form_list)
        print_debug("***********************************", 1)
        print_debug("Day6 - Custom Customs: Part2 ", 1)
        print_debug("The count of unanimous answers is: ")
        print_debug(str(my_form.get_yes_counts(my_form, True)), 1)

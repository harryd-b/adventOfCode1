from unittest import TestCase
from Util.file import load_file_to_list
from Day7.bags import Bags
from Util.util import print_debug


class TestBags(TestCase):
    DEBUG_ON = 1

    def test_recursive_bag_search(self):
        path = '../Resources/Day7.txt'
        bag_list = []
        my_bag = Bags
        load_file_to_list(path, bag_list)
        print_debug("***********************************", self.DEBUG_ON)
        print_debug("Day7 - Handy Haversacks: Part1 ", self.DEBUG_ON)
        print_debug("The count of outer bag types is: ", self.DEBUG_ON)
        bag_type_count = my_bag.get_outer_bag_types(my_bag, bag_list, 'shiny gold')
        print_debug(str(bag_type_count), self.DEBUG_ON)

    def test_recursive_bag_search_1(self):
        path = '../Resources/Day7.txt'
        bag_list = []
        my_bag_1 = Bags
        load_file_to_list(path, bag_list)
        print_debug("", self.DEBUG_ON)
        print_debug("***********************************", self.DEBUG_ON)
        print_debug("Day7 - Handy Haversacks: Part2 ", self.DEBUG_ON)
        print_debug("The count of inner bags: ", self.DEBUG_ON)
        total_bags = my_bag_1.get_inner_bags(my_bag_1, bag_list, 'shiny gold', 1)
        print_debug(str(total_bags), self.DEBUG_ON)

import unittest
from Day3.trees import count_trees_on_slope_1
from Util.util import print_debug
from Util.file import load_file_to_list


class TreeTestCase(unittest.TestCase):

    def test_across(self):
        tree_map = []
        load_file_to_list('../venv/Include/Day3.txt', tree_map)
        first_count = count_trees_on_slope_1(1, 1, tree_map)
        second_count = count_trees_on_slope_1(3, 1, tree_map)
        third_count = count_trees_on_slope_1(5, 1, tree_map)
        fourth_count = count_trees_on_slope_1(7, 1, tree_map)
        print_debug("***********************************")
        print_debug("Day3 - Toboggan Trajectory: Part1 ")
        print_debug("The counts of #'s encountered are: ")
        print_debug("First: " + str(first_count))
        print_debug("")
        print_debug("Second: " + str(second_count))
        print_debug("")
        print_debug("Third: " + str(third_count))
        print_debug("")
        print_debug("Fourth: " + str(fourth_count))
        print_debug("")
        print_debug("For the Slope: Right 3, Down 1 the count of trees encountered is :")
        print_debug(second_count)
        self.assertEqual(second_count, 191)

    def test_across_down(self):
        tree_map = []
        load_file_to_list('../venv/Include/Day3.txt', tree_map)
        first_count = count_trees_on_slope_1(1, 1, tree_map)
        second_count = count_trees_on_slope_1(3, 1, tree_map)
        third_count = count_trees_on_slope_1(5, 1, tree_map)
        fourth_count = count_trees_on_slope_1(7, 1, tree_map)
        fifth_count = count_trees_on_slope_1(1, 2, tree_map)
        print_debug("")
        print_debug("***********************************")
        print_debug("Day3 - Toboggan Trajectory: Part2 ")
        print_debug("The counts of #'s encountered are: ")
        print_debug("First: " + str(first_count))
        print_debug("")
        print_debug("Second: " + str(second_count))
        print_debug("")
        print_debug("Third: " + str(third_count))
        print_debug("")
        print_debug("Fourth: " + str(fourth_count))
        print_debug("")
        print_debug("Fifth: " + str(fifth_count))
        print_debug("")
        print_debug("If you multiply the counts for each slope you get:")
        test_product = first_count * second_count * third_count * fourth_count * fifth_count
        print_debug("Total Product = " + str(test_product))
        self.assertEqual(test_product, 1478615040)

    def test_down(self):
        tree_map = []
        load_file_to_list('../venv/Include/Day3.txt', tree_map)
        fifth_count = count_trees_on_slope_1(1, 2, tree_map)
        print_debug("Fifth: " + str(fifth_count))
        print_debug("")
        self.assertEqual(fifth_count, 32)
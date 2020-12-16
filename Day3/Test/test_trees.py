from unittest import TestCase
from Day3.trees import Trees
from Util.util import print_debug
from Util.file import load_file_to_list


class TestTrees(TestCase):
    def test_across(self):
        tree_map = []
        load_file_to_list('../Resources/Day3.txt', tree_map)
        first_count = Trees.count_trees_on_slope(1, 1, tree_map)
        second_count = Trees.count_trees_on_slope(3, 1, tree_map)
        third_count = Trees.count_trees_on_slope(5, 1, tree_map)
        fourth_count = Trees.count_trees_on_slope(7, 1, tree_map)
        print_debug("***********************************", 1)
        print_debug("Day3 - Toboggan Trajectory: Part1 ", 1)
        print_debug("The counts of #'s encountered are: ", 1)
        print_debug("First: " + str(first_count), 1)
        print_debug("", 1)
        print_debug("Second: " + str(second_count), 1)
        print_debug("", 1)
        print_debug("Third: " + str(third_count), 1)
        print_debug("", 1)
        print_debug("Fourth: " + str(fourth_count), 1)
        print_debug("", 1)
        print_debug("For the Slope: Right 3, Down 1 the count of trees encountered is :", 1)
        print_debug(second_count, 1)
        self.assertEqual(second_count, 191)

    def test_across_down(self):
        tree_map = []
        load_file_to_list('../Resources/Day3.txt', tree_map)
        first_count = Trees.count_trees_on_slope(1, 1, tree_map)
        second_count = Trees.count_trees_on_slope(3, 1, tree_map)
        third_count = Trees.count_trees_on_slope(5, 1, tree_map)
        fourth_count = Trees.count_trees_on_slope(7, 1, tree_map)
        fifth_count = Trees.count_trees_on_slope(1, 2, tree_map)
        print_debug("", 1)
        print_debug("***********************************", 1)
        print_debug("Day3 - Toboggan Trajectory: Part2 ", 1)
        print_debug("The counts of #'s encountered are: ", 1)
        print_debug("First: " + str(first_count), 1)
        print_debug("", 1)
        print_debug("Second: " + str(second_count), 1)
        print_debug("", 1)
        print_debug("Third: " + str(third_count), 1)
        print_debug("", 1)
        print_debug("Fourth: " + str(fourth_count), 1)
        print_debug("", 1)
        print_debug("Fifth: " + str(fifth_count), 1)
        print_debug("", 1)
        print_debug("If you multiply the counts for each slope you get:", 1)
        test_product = first_count * second_count * third_count * fourth_count * fifth_count
        print_debug("Total Product = " + str(test_product), 1)
        self.assertEqual(test_product, 1478615040)

    def test_down(self):
        tree_map = []
        load_file_to_list('../Resources/Day3.txt', tree_map)
        fifth_count = Trees.count_trees_on_slope(1, 2, tree_map)
        print_debug("Fifth: " + str(fifth_count), 1)
        print_debug("", 1)
        self.assertEqual(fifth_count, 32)
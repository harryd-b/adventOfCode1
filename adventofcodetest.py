import unittest
from file import load_file_to_list
from trees import count_trees_on_slope_1
from ppt import *


class TreeTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_down(self):
        tree_map = []
        load_file_to_list('venv/Include/trees.txt', tree_map)
        # load_file_to_list('venv/Include/smalltrees.txt', tree_map)

        fifth_count = count_trees_on_slope_1(1, 2, tree_map)
        print("Fifth: " + str(fifth_count))
        print("")
        # self.assertEqual(fifth_count, 2)
        self.assertEqual(fifth_count, 32)

    def test_across(self):
        tree_map = []
        # load_file_to_list('venv/Include/trees.txt', treeMap)
        load_file_to_list('venv/Include/smalltrees.txt', tree_map)
        first_count = count_trees_on_slope_1(1, 1, tree_map)
        second_count = count_trees_on_slope_1(3, 1, tree_map)
        third_count = count_trees_on_slope_1(5, 1, tree_map)
        fourth_count = count_trees_on_slope_1(7, 1, tree_map)

        print("The counts of #'s encountered are: ")
        print("First: " + str(first_count))
        print("")
        print("Second: " + str(second_count))
        print("")
        print("Third: " + str(third_count))
        print("")
        print("Fourth: " + str(fourth_count))
        print("")

        test_count = first_count * second_count * third_count * fourth_count
        print("Total Product = " + str(test_count))
        self.assertEqual(test_count, 168)

    def test_across_down(self):
        tree_map = []
        load_file_to_list('venv/Include/trees.txt', tree_map)
        # load_file_to_list('venv/Include/smalltrees.txt', tree_map)
        first_count = count_trees_on_slope_1(1, 1, tree_map)
        second_count = count_trees_on_slope_1(3, 1, tree_map)
        third_count = count_trees_on_slope_1(5, 1, tree_map)
        fourth_count = count_trees_on_slope_1(7, 1, tree_map)
        fifth_count = count_trees_on_slope_1(1, 2, tree_map)

        print("The counts of #'s encountered are: ")
        print("First: " + str(first_count))
        print("")
        print("Second: " + str(second_count))
        print("")
        print("Third: " + str(third_count))
        print("")
        print("Fourth: " + str(fourth_count))
        print("")
        print("Fifth: " + str(fifth_count))
        print("")
        print("Total Product = " + str(first_count * second_count * third_count * fourth_count * fifth_count))

        test_count = first_count * second_count * third_count * fourth_count * fifth_count
        print("Total Product = " + str(test_count))
        # self.assertEqual(test_count, 336)
        self.assertEqual(test_count, 1478615040)


class PassportTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()

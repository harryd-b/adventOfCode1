# Python3 program to find all pairs in
# a list of integers with given sum
from itertools import combinations
from Util.file import load_file_to_list
import copy


def findPairs(list_of_numbers, sum_to_find):
    return [pair for pair in combinations(map(int, list_of_numbers), 2) if sum(pair) == int(sum_to_find)]


def loop_through_set(my_xmas_data):
    for i in range(len(my_xmas_data)):
        if i >= 25:
            xmas_data_prev_25 = copy.deepcopy(my_xmas_data[i - 25:i])
            pairs = findPairs(xmas_data_prev_25, my_xmas_data[i])
            if pairs:
                continue
            else:
                print("First value that isn't a sum of two of the previous 25 numbers is: ")
                print(my_xmas_data[i])
                break


# Function to print sublist having given sum using Hashing
def findSublist(xmas_list, my_sum):
    # insert (0, -1) pair into the set to handle the case when
    # sublist with given sum starts from index 0
    dict = {0: -1}

    # maintains sum of elements so far
    sum_so_far = 0

    # traverse the given list
    for i in range(len(xmas_list)):

        # update sum_so_far
        sum_so_far += xmas_list[i]

        # if (sum_so_far - my_sum) is seen before, we have found
        # the sublist with sum 'my_sum'
        if (sum_so_far - my_sum) in dict:
            contiguous_sub_array = copy.deepcopy(xmas_list[dict.get(sum_so_far - my_sum) + 1:i + 1])
            print("Sublist found", (dict.get(sum_so_far - my_sum) + 1, i))
            print(contiguous_sub_array)
            print("Sum of contiguous sub_array")
            print(sum(contiguous_sub_array))
            print("Largest Number:")
            print(max(contiguous_sub_array))
            print("Smallest Number:")
            print(min(contiguous_sub_array))
            print("Sum:")
            print(min(contiguous_sub_array) + max(contiguous_sub_array))
            return

        # insert current sum with index into the dict
        dict[sum_so_far] = i


if __name__ == '__main__':
    xmas_data = []
    path = '../venv/Include/xmas.txt'
    load_file_to_list(path, xmas_data)
    print("Day 8: Part 1:")
    loop_through_set(xmas_data)
    print("")
    print("Day 8: Part 2:")
    findSublist(list(map(int, xmas_data)), 731031916)

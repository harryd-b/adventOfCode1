

def count_trees_on_slope_1(right_shift, down_shift, treemap):

    tree_map = treemap
    counter = 0
    counter1 = 0
    length_of_list = len(list(tree_map[0]))

    j = 0
    for i in range(len(tree_map)):

        j += down_shift

        if j >= len(tree_map):
            break

        counter += right_shift

        if counter >= length_of_list:
            counter = (counter - length_of_list)

        if list(tree_map[j])[counter] == '#':
            counter1 += 1

    return counter1




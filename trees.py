

def count_trees_on_slope_1(right_shift, down_shift, treemap):
    print("count_trees_on_slope_1 - Right Shift: " + str(right_shift) + " Down Shift: " + str(down_shift))
    tree_map = treemap
    counter = 0
    counter1 = 0
    length_of_list = len(list(tree_map[0]))
    print(length_of_list)
    j = 0
    for i in range(len(tree_map)):

        j += down_shift

        if j >= len(tree_map):
            print("last line")
            break

        print("This is line: " + str(j + 1))
        print(tree_map[j])
        counter += right_shift

        if counter >= length_of_list:
            counter = (counter - length_of_list)

        if list(tree_map[j])[counter] == '#':
            counter1 += 1
            print("Counter1: ********* " + str(counter1))

        print("Character " + str(counter + 1) + " is " + list(tree_map[j])[counter])
    return counter1




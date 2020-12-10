from file import load_file_to_list
import re
bag_type_count = 0
recursion_level = 0
no_repeat = []

bag_type_count_1 = 0
recursion_level_1 = 0
total_bags = 0


def recursive_bag_search(bag_list, bag_type):
    for i in range(len(bag_list)):
        global bag_type_count
        global recursion_level

        first_split = bag_list[i].split(" bags contain ")
        outer_bag = first_split[0]

        inner_bags = first_split[1]
        if inner_bags.find(bag_type) > 0:
            recursion_level += 1
            if outer_bag not in no_repeat:
                bag_type_count += 1
                recursive_bag_search(bag_list, outer_bag)
                no_repeat.append(outer_bag)
        recursion_level -= 1


def recursive_bag_search_1(bag_list, bag_type, bag_count):
    global bag_type_count_1
    global recursion_level_1
    global total_bags

    for i in range(len(bag_list)):
        first_split = bag_list[i].split(" bags contain ")
        outer_bag = first_split[0]

        if outer_bag == bag_type:

            inner_bags = first_split[1]

            inner_bag_list = inner_bags[:-1].split(", ")

            # get the bag counts
            bag_type_counts = re.findall(r'\d+', inner_bags)

            # now we need to get the number at the beginning of each bag_type
            for j in range(len(inner_bag_list)):
                # beginning (only works with single digits) and bag or bags from the end
                my_bag_type = inner_bag_list[j][2:].replace(" bags", "").replace(" bag", "")
                if my_bag_type == " other":
                    continue
                my_bag_count = int(bag_type_counts[j])
                new_bag_count = bag_count * my_bag_count
                total_bags += new_bag_count

                recursive_bag_search_1(bag_list, my_bag_type, new_bag_count)


def pack_bags_and_search():
    path = 'venv/Include/bags.txt'
    bag_list = []

    load_file_to_list(path, bag_list)

    print("Day 7 Part 1:")
    recursive_bag_search(bag_list, 'shiny gold')
    print(str(bag_type_count))

    print("Day 7 Part 2:")
    recursive_bag_search_1(bag_list, 'shiny gold', 1)
    print(str(total_bags))


if __name__ == '__main__':
    pack_bags_and_search()

from Util.file import load_file_to_list
import re

bag_type_count = 0
recursion_level = 0
no_repeat = []

bag_type_count_1 = 0
recursion_level_1 = 0
total_bags = 0


class Bags:
    def recursive_bag_search(self, bag_list, bag_type):
        global bag_type_count
        global recursion_level
        global no_repeat

        for i in range(len(bag_list)):
            first_split = bag_list[i].split(" bags contain ")
            outer_bag = first_split[0]

            inner_bags = first_split[1]
            if inner_bags.find(bag_type) > 0:
                recursion_level += 1
                if outer_bag not in no_repeat:
                    bag_type_count += 1
                    self.recursive_bag_search(self, bag_list, outer_bag)
                    no_repeat.append(outer_bag)
            recursion_level -= 1

    def recursive_bag_search_1(self, bag_list, bag_type, bag_count):
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

                    self.recursive_bag_search_1(self, bag_list, my_bag_type, new_bag_count)

    def get_inner_bags(self, bag_list, bag_type, bag_count):
        self.recursive_bag_search_1(self, bag_list, bag_type, bag_count)
        return total_bags

    def get_outer_bag_types(self, bag_list, bag_type):
        self.recursive_bag_search(self, bag_list, bag_type)
        return bag_type_count

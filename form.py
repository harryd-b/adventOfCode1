from file import load_file_to_list

# needs refactoring


def load_loop():
    form_map = []
    load_file_to_list('venv/Include/form.txt', form_map)

    group_count = 0
    group_form_list = []
    group_member_count = 0
    group_num_list = []
    for i in range(len(form_map)):
        line = form_map[i]

        # have we reached a new group?
        if line == "":

            # add the number of people in this group to the list
            group_num_list.append(group_member_count)

            # increment the group counter
            group_count += 1

            # create a new group
            group_form_list.append("")

            # reset the counter of group members
            group_member_count = 0
            continue

        if len(group_form_list) == 0:
            group_form_list = [""]
        group_form_list[group_count] = group_form_list[group_count] + line
        group_member_count += 1

        # last line?
        if i == len(form_map) - 1:
            group_num_list.append(group_member_count)
    form_sum = 0

    unique_group_list = []
    for i in range(len(group_form_list)):
        unique_group_list.append(''.join(set(group_form_list[i])))
        form_sum += len(unique_group_list[i])

    total_count = 0

    for i in range(len(unique_group_list)):
        my_list = list(unique_group_list[i])

        for j in range(len(my_list)):
            my_count = group_form_list[i].count(my_list[j])

            if my_count == group_num_list[i]:
                total_count += 1

    print(str(total_count))


if __name__ == '__main__':
    load_loop()

class Forms:
    group_form_list = []
    group_num_list = []

    def get_groups(self, form_list):
        group_count = 0
        group_member_count = 0
        for i in range(len(form_list)):
            line = form_list[i]

            # have we reached a new group?
            if line == "":
                # add the number of people in this group to the list
                self.group_num_list.append(group_member_count)

                # increment the group counter
                group_count += 1

                # create a new group
                self.group_form_list.append("")

                # reset the counter of group members
                group_member_count = 0
                continue

            if len(self.group_form_list) == 0:
                self.group_form_list = [""]
            self.group_form_list[group_count] = self.group_form_list[group_count] + line
            group_member_count += 1

            # last line?
            if i == len(form_list) - 1:
                self.group_num_list.append(group_member_count)

    def get_yes_counts(self, unanimous):
        form_sum = 0
        unique_group_list = []
        for i in range(len(self.group_form_list)):
            unique_group_list.append(''.join(set(self.group_form_list[i])))
            form_sum += len(unique_group_list[i])

        total_unanimous_count = 0
        total_count = 0

        for i in range(len(unique_group_list)):
            my_list = list(unique_group_list[i])
            total_count += len(my_list)
            for j in range(len(my_list)):
                my_count = self.group_form_list[i].count(my_list[j])

                if my_count == self.group_num_list[i]:
                    total_unanimous_count += 1

        if unanimous:
            return total_unanimous_count
        else:
            return total_count

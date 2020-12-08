def load_file_to_list(path, linelist):
    # open file and read the content in a list
    with open(path, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            current_line = line[:-1]

            # add item to the list
            linelist.append(current_line)


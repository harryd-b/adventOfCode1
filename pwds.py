# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def check_pwd(pwd, lownum, hinum, chkchar):
    # Use a breakpoint in the code line below to debug your script.

    if int(lownum) <= pwd.count(chkchar) <= int(hinum):
        return 1
    else:
        return 0


def check_pwd_1(pwd, lownum, hinum, chkchar):

    char_list = list(pwd)

    if char_list[int(lownum)-1] == chkchar:
        if char_list[int(hinum) - 1] == chkchar:
            return 0
        else:
            return 1
    elif char_list[int(hinum) - 1] == chkchar:
        return 1
    else:
        return 0


def load_file(path, passwordsmap):
    # open file and read the content in a list
    with open(path, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            current_password_map = line[:-1]

            # add item to the list
            passwordsmap.append(current_password_map)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # define an empty list

    passwordsMap = []
    load_file('venv/Include/pwd_list.txt', passwordsMap)

    # print(passwordsMap)

    counter = 0
    counter1 = 0
    for i in range(len(passwordsMap)):
        firstSplit = []
        firstSplit = passwordsMap[i].split(": ")
        password = firstSplit[1]
        secondSplit = firstSplit[0].split(" ")
        checkCharacter = secondSplit[1]
        thirdSplit = secondSplit[0].split("-")
        lowNumber = thirdSplit[0]
        highNumber = thirdSplit[1]
        counter += check_pwd(password, lowNumber, highNumber, checkCharacter)
        counter1 += check_pwd_1(password, lowNumber, highNumber, checkCharacter)
    print(counter)
    print(counter1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Passwords:

    @staticmethod
    def check_pwd(pwd, low_num, hi_num, chk_char):
        if int(low_num) <= pwd.count(chk_char) <= int(hi_num):
            return 1
        else:
            return 0

    @staticmethod
    def check_pwd_1(pwd, low_num, hi_num, chk_char):
        char_list = list(pwd)

        if char_list[int(low_num) - 1] == chk_char:
            if char_list[int(hi_num) - 1] == chk_char:
                return 0
            else:
                return 1
        elif char_list[int(hi_num) - 1] == chk_char:
            return 1
        else:
            return 0

    @staticmethod
    def split_data(password):
        first_split = password.split(": ")
        password = first_split[1]
        second_split = first_split[0].split(" ")
        check_character = second_split[1]
        third_split = second_split[0].split("-")
        low_number = third_split[0]
        high_number = third_split[1]
        return password, low_number, high_number, check_character

    @staticmethod
    def check_all(passwords_list, part):
        counter = 0
        for i in range(len(passwords_list)):
            check_list = Passwords.split_data(passwords_list[i])
            if part == 1:
                counter += Passwords.check_pwd(check_list[0], check_list[1], check_list[2], check_list[3])
            else:
                counter += Passwords.check_pwd_1(check_list[0], check_list[1], check_list[2], check_list[3])
        return counter

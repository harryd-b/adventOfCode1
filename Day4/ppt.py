class Passport:
    byr = ""  # (Birth Year)
    iyr = ""  # (Issue Year)
    eyr = ""  # (Expiration Year)
    hgt = ""  # (Height)
    hcl = ""  # (Hair Color)
    ecl = ""  # (Eye Color)
    pid = ""  # (Passport ID)
    cid = ""  # (Country ID)

    def is_passport_valid_2(self):
        if self.byr != "" and self.iyr != "" and self.eyr != "" and self.hgt != "" and self.hcl != "" and self.ecl != "":
            if self.pid != "" and self.check_byr() and self.check_eyr() and self.check_iyr() and self.check_hgt():
                if self.check_hcl() and self.check_ecl() and self.check_pid():
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    def is_passport_valid_1(self):
        if self.byr != "" and self.iyr != "" and self.eyr != "" and self.hgt != "":
            if self.pid != "" and self.hcl != "" and self.ecl != "":
                return 1
            else:
                return 0
        else:
            return 0

    def check_byr(self):
        if 2002 >= int(self.byr) >= 1920:
            return 1
        else:
            return 0

    def check_iyr(self):
        if 2010 <= int(self.iyr) <= 2020:
            return 1
        else:
            return 0

    def check_eyr(self):
        if 2020 <= int(self.eyr) <= 2030:
            return 1
        else:
            return 0

    def check_hgt(self):
        string_length = int(len(self.hgt) - 2)
        my_hgt = self.hgt
        if self.hgt[-2:] == "cm":
            if 150 <= int(my_hgt[0:string_length]) <= 193:
                return 1
            else:
                return 0
        elif self.hgt[-2:] == "in":
            if 59 <= int(my_hgt[0:string_length]) <= 76:
                return 1
            else:
                return 0
        else:
            return 0

    def check_hcl(self):
        if self.hcl != "":

            if self.hcl[0] == "#" and self.hcl[-6:].isalnum() and len(self.hcl) == 7:
                return 1
            else:
                return 0
        else:
            return 0

    def check_ecl(self):
        list_of_options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if self.ecl in list_of_options:
            return 1
        else:
            return 0

    def check_pid(self):
        if self.pid.isnumeric() and len(self.pid) == 9:
            return 1
        else:
            return 0

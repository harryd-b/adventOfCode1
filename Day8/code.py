from Util.file import load_file_to_list
import copy


class Boot:
    accumulator = 0

    def boot_bug_finder(self, instruction_list):
        i = 0
        test_instruction_list = copy.deepcopy(instruction_list)
        while not self.boot(self, test_instruction_list) and i in range(len(instruction_list)):
            test_instruction_list = copy.deepcopy(instruction_list)
            self.fix_bug(self, test_instruction_list, i)
            i += 1
        return i

    def boot(self, instructions):
        self.accumulator = 0
        position = 0
        previous_positions = []
        no_repeat = True
        while no_repeat and position in range(len(instructions)):
            instruction_split = instructions[position].split(" ")
            plus_minus = instruction_split[1][:1]
            number_of_moves = instruction_split[1][1:]
            if instruction_split[0] == "nop":
                previous_positions.append(position)
                position += 1
            elif instruction_split[0] == "acc":
                if plus_minus == "+":
                    self.accumulator += int(number_of_moves)
                else:
                    self.accumulator -= int(number_of_moves)
                previous_positions.append(position)
                position += 1
            elif instruction_split[0] == "jmp":
                previous_positions.append(position)
                if plus_minus == "+":
                    if number_of_moves.isdigit():
                        position += int(number_of_moves)
                    else:
                        break
                else:
                    position -= int(number_of_moves)

            if position in previous_positions:
                no_repeat = False
        return no_repeat

    def get_accumulator(self):
        return self.accumulator

    def fix_bug(self, instructions, line):
        if instructions[line].find("jmp") >= 0:
            instructions[line] = instructions[line].replace("jmp", "nop")
        elif instructions[line].find("nop") >= 0:
            instructions[line] = instructions[line].replace("nop", "jmp")

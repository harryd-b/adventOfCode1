from file import load_file_to_list
import copy


def load_and_boot():
    instruction_list = []
    path = 'venv/Include/code.txt'
    load_file_to_list(path, instruction_list)
    boot(instruction_list)


def boot_bug_finder():
    instruction_list = []
    path = 'venv/Include/code.txt'
    load_file_to_list(path, instruction_list)
    i = 0
    test_instruction_list = copy.deepcopy(instruction_list)
    while not boot(test_instruction_list) and i in range(len(instruction_list)):
        test_instruction_list = copy.deepcopy(instruction_list)
        if instruction_list[i].find("jmp") >= 0:
            test_instruction_list[i] = test_instruction_list[i].replace("jmp", "nop")
        elif instruction_list[i].find("nop") >= 0:
            test_instruction_list[i] = test_instruction_list[i].replace("nop", "jmp")
        i += 1
    print("Bug Found at Line: ")
    print(i)


def boot(instructions):
    accumulator = 0
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
                accumulator += int(number_of_moves)
            else:
                accumulator -= int(number_of_moves)
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
    print("Accumulator = ")
    print(accumulator)
    return no_repeat


if __name__ == '__main__':
    print("Load and Boot")
    load_and_boot()
    print("")
    print("Bug Finder")
    boot_bug_finder()

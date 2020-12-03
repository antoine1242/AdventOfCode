import math
import copy
import itertools
import numpy as np
import matplotlib.pyplot as plt

def main():
    with open("input.txt") as f:
        content = f.readline()
    opcodes = content.split(",")
    while len(opcodes) < 100000:
        opcodes.append("0")
    
    direction = "U"
    current_position = [250, 250]
    current_output = ("0", "0", 0 ,0)
    grid = np.full((501, 501), ".")
    grid[250,250] = "#"
    positions_set = set()
    positions_set.add("500,500")

    while current_output[0] != "99":
        current_input = get_color(current_position, grid)
        current_output = get_output(opcodes, current_input, current_output[2], current_output[3])
        if current_output[0] == "99":
            break

        if current_output[0] == "0":
            paint(grid, ".", current_position)
        else:
            paint(grid, "#", current_position)

        if direction == "U":
            if current_output[1] == "0":
                direction = "L"
                current_position[1] -= 1
            else:
                direction = "R"
                current_position[1] += 1
        elif direction == "L":
            if current_output[1] == "0":
                direction = "D"
                current_position[0] += 1
            else:
                direction = "U"
                current_position[0] -= 1
        elif direction == "D":
            if current_output[1] == "0":
                direction = "R"
                current_position[1] += 1
            else:
                direction = "L"
                current_position[1] -= 1
        elif direction == "R":
            if current_output[1] == "0":
                direction = "U"
                current_position[0] -= 1
            else:
                direction = "D"
                current_position[0] += 1

        position_string = str(current_position[0]) + "," + str(current_position[1])
        
        if position_string not in positions_set:
            positions_set.add(position_string)

    int_array = []

    for index_line, line in enumerate(grid):
        int_array.append([])
        for index_column, column in enumerate(line):
            if grid[index_line, index_column] == ".":
                int_array[index_line].append(0)
            else:
                int_array[index_line].append(1)

    

    plt.imshow(np.array(int_array))
    plt.show()

def paint(grid, color, current_position):
    grid[current_position[0], current_position[1]] = color

def get_color(current_position, grid):
    if grid[current_position[0]][current_position[1]] == ".":
        return 0
    
    return 1

def get_output(opcodes, current_input, i, relative_base):
    i = i
    relative_base = relative_base
    arguments = []

    while i < len(opcodes):
        operation, mode1, mode2, mode3 = readOpcode(opcodes[i])
        if operation == 99:
            return ("99", 0, i, relative_base)

        if operation == 1:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes, mode2, 2, i, relative_base)
            argument3 = get_argument_write(opcodes, mode3, 3, i, relative_base)

            opcodes[argument3] = str(argument1 + argument2)
            i += 4

        elif operation == 2:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes, mode2, 2, i, relative_base)
            argument3 = get_argument_write(opcodes, mode3, 3, i, relative_base)

            opcodes[argument3] = str(argument1 * argument2)
            i += 4

        elif operation == 3:
            argument1 = get_argument_write(opcodes, mode1, 1, i, relative_base)

            opcodes[argument1] = str(current_input)
            i += 2

        elif operation == 4:
            argument1 = get_argument_read(opcodes,mode1, 1, i, relative_base)
            
            arguments.append(str(argument1))
            i += 2
            if len(arguments) == 2:
                return (arguments[0], arguments[1], i, relative_base)

        elif operation == 5:
            argument1 = get_argument_read(opcodes,mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes,mode2, 2, i, relative_base)

            if argument1 != 0:
                i = argument2
            else:
                i += 3

        elif operation == 6:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes, mode2, 2, i, relative_base)

            if argument1 == 0:
                i = argument2
            else:
                i += 3

        elif operation == 7:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes, mode2, 2, i, relative_base)
            argument3 = get_argument_write(opcodes, mode3, 3, i, relative_base)

            if argument1 < argument2:
                opcodes[argument3] = str(1)
            else:
                opcodes[argument3] = str(0)
            i += 4

        elif operation == 8:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)
            argument2 = get_argument_read(opcodes, mode2, 2, i, relative_base)
            argument3 = get_argument_write(opcodes, mode3, 3, i, relative_base)

            if argument1 == argument2:
                opcodes[argument3] = str(1)
            else:
                opcodes[argument3] = str(0)
            i += 4

        elif operation == 9:
            argument1 = get_argument_read(opcodes, mode1, 1, i, relative_base)

            relative_base += argument1
            i += 2

    return opcodes[0]

def get_argument_read(opcodes, mode, argument_number, i, relative_base):
    if mode == 0:
        argument = int(opcodes[int(opcodes[i+argument_number])])
    elif mode == 1:
        argument = int(opcodes[i+argument_number])
    elif mode == 2:
        argument = int(opcodes[int(opcodes[i+argument_number]) + relative_base])

    return argument

def get_argument_write(opcodes, mode, argument_number, i, relative_base):
    if mode == 0:
        argument = int(opcodes[i+argument_number])
    elif mode == 2:
        argument = int(opcodes[i+argument_number]) + relative_base
    else:
        print("INVALID MODE3")

    return argument

def readOpcode(opcode):
    mode1 = mode2 = mode3 = 0
    operation = int(opcode[-1])
    
    if len(opcode) >= 2:
        operation = int(opcode[-2:])

    if len(opcode) > 2:
        mode1 = int(opcode[-3])
    
    if len(opcode) > 3:
        mode2 = int(opcode[-4])

    if len(opcode) > 4:
        mode3 = int(opcode[-5])

    return operation, mode1, mode2, mode3

main()
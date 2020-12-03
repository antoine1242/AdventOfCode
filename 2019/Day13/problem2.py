import math
import copy
import itertools
import numpy as np

def main():
    with open("input.txt") as f:
        content = f.readline()
    opcodes = content.split(",")
    while len(opcodes) < 100000:
        opcodes.append("0")

    opcodes[0] = 2
    
    grid = np.full((100, 100), " ")
    grid = grid.tolist()

    simulate_game(opcodes, grid, 0)


def paint(grid, color, current_position):
    grid[current_position[0], current_position[1]] = color

def get_color(current_position, grid):
    if grid[current_position[0]][current_position[1]] == ".":
        return 0
    
    return 1

def simulate_game(opcodes, grid, current_input):
    i = 0
    relative_base = 0
    arguments = []
    block_count = 0

    while i < len(opcodes):
        operation, mode1, mode2, mode3 = readOpcode(opcodes[i])
        if operation == 99:
            break

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
            opcodes[argument1] = current_input

            i += 2

        elif operation == 4:
            argument1 = get_argument_read(opcodes,mode1, 1, i, relative_base)
            
            arguments.append(str(argument1))
            i += 2
            if len(arguments) == 3:
                column = int(arguments[1])
                row = int(arguments[0])
                tile_type = int(arguments[2])
                
                if grid[row][column] == "BL":
                    block_count -= 1
                if tile_type == 0:
                    grid[row][column] = " "
                elif tile_type == 1:
                    grid[row][column] = "W"
                elif tile_type == 2:
                    grid[row][column] = "BL"
                    block_count += 1
                elif tile_type == 3:
                    grid[row][column] = "H"
                elif tile_type == 4:
                    grid[row][column] = "B"

                arguments = []

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

    print(block_count)

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
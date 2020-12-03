import math
import copy
import itertools

def main():
    with open("input.txt") as f:
        content = f.readline()
    initial_opcodes = content.split(",")

    while len(initial_opcodes) < 100000:
        initial_opcodes.append("0")

    get_output(initial_opcodes, 1)

def get_output(opcodes, currentInput):#1, currentInput2=0):
    i = 0
    #input1_used = False
    relative_base = 0

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

            opcodes[argument1] = str(currentInput)
            i += 2

        elif operation == 4:
            argument1 = get_argument_read(opcodes,mode1, 1, i, relative_base)
            print(argument1)

            i += 2

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
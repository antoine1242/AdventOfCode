import math
import copy
import itertools

def main():
    with open("input.txt") as f:
        content = f.readline()
    initial_opcodes = content.split(",")

    max_value = 0

    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))

    for permutation in permutations:
        opcodesA = copy.deepcopy(initial_opcodes)
        outputA = get_output(opcodesA, permutation[0], 0)

        opcodesB = copy.deepcopy(initial_opcodes)
        outputB = get_output(opcodesB, permutation[1], outputA)

        opcodesC = copy.deepcopy(initial_opcodes)
        outputC = get_output(opcodesC, permutation[2], outputB)

        opcodesD = copy.deepcopy(initial_opcodes)
        outputD = get_output(opcodesD, permutation[3], outputC)

        opcodesE = copy.deepcopy(initial_opcodes)
        outputE = get_output(opcodesE, permutation[4], outputD)

        if outputE > max_value:
            max_value = outputE

    print(max_value)

def get_output(opcodes, currentInput1, currentInput2):
    i = 0
    input1_used = False

    while i < len(opcodes):
        operation, mode1, mode2, mode3 = readOpcode(opcodes[i])
        if operation == 99:
            break

        if operation == 1:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])
            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            argument3 = int(opcodes[i+3])

            opcodes[argument3] = str(argument1 + argument2)
            i += 4

        elif operation == 2:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])
            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            argument3 = int(opcodes[i+3])

            opcodes[argument3] = str(argument1 * argument2)
            i += 4

        elif operation == 3:
            argument1 = int(opcodes[i+1])

            if not input1_used:
                opcodes[argument1] = str(currentInput1)
                input1_used = True
            else:
                opcodes[argument1] = str(currentInput2)
            i += 2

        elif operation == 4:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])

            return argument1

        elif operation == 5:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])

            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            if argument1 !=0:
                i = argument2
            else:
                i += 3

        elif operation == 6:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])
            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            if argument1 == 0:
                i = argument2
            else:
                i += 3

        elif operation == 7:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])
            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            argument3 = int(opcodes[i+3])

            if argument1 < argument2:
                opcodes[argument3] = str(1)
            else:
                opcodes[argument3] = str(0)
            i += 4

        elif operation == 8:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])
            if mode2 == 0:
                argument2 = int(opcodes[int(opcodes[i+2])])
            else:
                argument2 = int(opcodes[i+2])

            argument3 = int(opcodes[i+3])

            if argument1 == argument2:
                opcodes[argument3] = str(1)
            else:
                opcodes[argument3] = str(0)
            i += 4

        else:
            return 0

    return opcodes[0]

def readOpcode(opcode):
    mode1 = mode2 = mode3 = 0
    operation = int(opcode[-1])
    
    if len(opcode) >= 2:
        operation = int(opcode[-2:])

    if len(opcode) > 2:
        mode1 = int(opcode[-3])
    
    if len(opcode) > 3:
        mode2 = int(opcode[-4])

    return operation, mode1, mode2, mode3

main()
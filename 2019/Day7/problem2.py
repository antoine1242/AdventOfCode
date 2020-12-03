import math
import copy
import itertools
import time

def main():
    with open("input.txt") as f:
        content = f.readline()
    initial_opcodes = content.split(",")

    max_signal = 0

    permutations = list(itertools.permutations([5, 6, 7, 8, 9]))

    for permutation in permutations:
        opcodesA = copy.deepcopy(initial_opcodes)
        opcodesB = copy.deepcopy(initial_opcodes)
        opcodesC = copy.deepcopy(initial_opcodes)
        opcodesD = copy.deepcopy(initial_opcodes)
        opcodesE = copy.deepcopy(initial_opcodes)

        signal = 0
        output_signal = 0

        signal, iA = get_output(opcodesA, 0, permutation[0], 0)
        signal, iB = get_output(opcodesB, 0, permutation[1], signal)
        signal, iC = get_output(opcodesC, 0, permutation[2], signal)
        signal, iD = get_output(opcodesD, 0, permutation[3], signal)
        signal, iE = get_output(opcodesE, 0, permutation[4], signal)

        while signal is not None:
            signal, iA = get_output(opcodesA, iA, signal)
            signal, iB = get_output(opcodesB, iB, signal)
            signal, iC = get_output(opcodesC, iC, signal)
            signal, iD = get_output(opcodesD, iD, signal)
            signal, iE = get_output(opcodesE, iE, signal)

            if signal is not None:
                output_signal = signal

        if output_signal > max_signal:
            max_signal = output_signal

    print(max_signal)    

def get_output(opcodes, current_i, current_input1, current_input2 = 0):
    i = current_i
    input1_used = False

    while i < len(opcodes):
        operation, mode1, mode2, mode3 = readOpcode(opcodes[i])
        if operation == 99:
            return None, i

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
                opcodes[argument1] = str(current_input1)
                input1_used = True
            else:
                opcodes[argument1] = str(current_input2)
            i += 2

        elif operation == 4:
            if mode1 == 0:
                argument1 = int(opcodes[int(opcodes[i+1])])
            else:
                argument1 = int(opcodes[i+1])

            i += 2
            return argument1, i

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

    return 0

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
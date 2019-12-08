import math
import copy

def get_output(opcodes):
    i = 0
    while i < len(opcodes):
        curr_op = opcodes[i][-2:]

        if len(opcodes[i]) >= 3:
            mode1 = opcodes[i][-3]
        else:
            mode1 = "0"
        if len(opcodes[i]) >= 4:
            mode2 = opcodes[i][-4]
        else:
            mode2 = "0"
        
        mode3 = "0"

        if curr_op == "01" or curr_op == "1":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]

            third = opcodes[i+3]

            opcodes[int(third)] = str(int(first) + int(second))
            i += 4

        elif curr_op == "02" or curr_op == "2":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]
            third = opcodes[i+3]

            opcodes[int(third)] = str(int(first) * int(second))
            i += 4

        elif curr_op == "05" or curr_op == "5":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]

            if int(first) != 0:
                i = int(second)
            else:
                i += 3

        elif curr_op == "06" or curr_op == "6":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]

            if int(first) == 0:
                i = int(second)
            else:
                i += 3

        elif curr_op == "07" or curr_op == "7":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]
            third = opcodes[i+3]

            if int(first) < int(second):
                opcodes[int(third)] = str(1)
            else:
                opcodes[int(third)] = str(0)
            i += 4

        elif curr_op == "08" or curr_op == "8":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            if mode2 == "0":
                second = opcodes[int(opcodes[i+2])]
            else:
                second = opcodes[i+2]
            third = opcodes[i+3]

            if int(first) == int(second):
                opcodes[int(third)] = str(1)
            else:
                opcodes[int(third)] = str(0)
            i += 4

        elif curr_op == "03" or curr_op == "3":
            opcodes[int(opcodes[i+1])] = 5 #int(input("enter int: "))
            i += 2
        elif curr_op == "04" or curr_op == "4":
            if mode1 == "0":
                first = opcodes[int(opcodes[i+1])]
            else:
                first = opcodes[i+1]
            print(first)
            i += 2
        elif curr_op == "99":
            break

        else:
            return 0  

    return opcodes[0]

with open("input.txt") as f:
    content = f.readline()
opcodes = content.split(",")
initial_opcodes = list(map(int, opcodes))

get_output(opcodes)

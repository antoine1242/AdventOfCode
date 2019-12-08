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

        elif curr_op == "03" or curr_op == "3":
            opcodes[int(opcodes[i+1])] = 1 #int(input("enter int: "))
            i += 2
        elif curr_op == "04" or curr_op == "4":
            print(opcodes[int(opcodes[i+1])])
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

print("len opcodes:", len(opcodes))
get_output(opcodes)

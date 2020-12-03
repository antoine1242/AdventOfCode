import math
import copy

with open("input1.txt") as f:
    content = f.readline()
opcodes = content.split(",")
opcodes = list(map(int, opcodes))

opcodes[1] = 12
opcodes[2] = 2

i = 0
while i < len(opcodes):
    if opcodes[i] == 1:
        opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

    elif opcodes[i] == 2:
        opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

    elif opcodes[i] == 99:
        break

    else:
        print("Something went wrong!")
        break

    i += 4

print(opcodes[0])

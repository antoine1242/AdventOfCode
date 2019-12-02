import math
import copy

def try_pair(initial_opcodes, i, j):
    opcodes = copy.deepcopy(initial_opcodes)
    opcodes[1] = i
    opcodes[2] = j
    output = get_output(opcodes)

    if output == 19690720:
        return (i,j)
    else:
        return (100,100)

def get_output(opcodes):
    i = 0
    while i < len(opcodes):
        if opcodes[i] == 1:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

        elif opcodes[i] == 2:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

        elif opcodes[i] == 99:
            break

        else:
            return 0

        i += 4

    return opcodes[0]

with open("input1.txt") as f:
    content = f.readline()
opcodes = content.split(",")
initial_opcodes = list(map(int, opcodes))

for i in range(100):
    for j in range(100):
        result = try_pair(initial_opcodes, i, j)
        if result[0] != 100:
            break
    if result[0] != 100:
        break
print(result)
print(100*result[0] + result[1])

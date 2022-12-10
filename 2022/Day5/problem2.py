import math
import copy

def main():
    with open("Day5/input.txt") as f:
        lines = f.read().split("\n\n")

    cargos = lines[0].split("\n")

    moves = lines[1].split("\n")

    stacks = []
    for i in range(9):
        stacks.append([])

    for line in cargos:

        i = 0
        curr_cargo = 0
        spaces_count = 0

        while i < len(line):
            if line[i] == " ":
                spaces_count += 1

            else:
                if spaces_count >= 1:
                    curr_cargo += spaces_count // 4

                i += 1
                if line[i] != " ":
                    stacks[curr_cargo].insert(0, line[i])
                i += 1

                spaces_count = 0
                curr_cargo += 1

            i += 1

    for move in moves:
        nb_crates = int(move.split(" from ")[0].split(" ")[1])

        incoming = int(move.split(" from ")[1].split(" ")[0]) - 1
        receiving = int(move.split(" from ")[1].split(" ")[2]) - 1 


        add_stack = []
        for i in range(nb_crates):
            add_stack.append(stacks[incoming].pop())

        for i in range(nb_crates):
            stacks[receiving].append(add_stack.pop())
        
    answer = ""
    for stack in stacks:
        answer += stack.pop()

    print(answer)

main()
import math
import copy

def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    total_trees = 0

    seen = set()
    
    for i in range(len(lines)):
        curr_tallest = -1
        for j in range(len(lines[0])):
            if int(lines[i][j]) > curr_tallest:
                if (i, j) not in seen:
                    seen.add((i,j))
                    total_trees += 1
                curr_tallest = int(lines[i][j])

    for i in range(len(lines)):
        curr_tallest = -1
        for j in range(len(lines[0])-1, 0, -1):
            if int(lines[i][j]) > curr_tallest:
                if (i, j) not in seen:
                    seen.add((i,j))
                    total_trees += 1
                curr_tallest = int(lines[i][j])

    for j in range(len(lines[0])):
        curr_tallest = -1
        for i in range(len(lines)):
            if int(lines[i][j]) > curr_tallest:
                if (i, j) not in seen:
                    seen.add((i,j))
                    total_trees += 1
                curr_tallest = int(lines[i][j])

    for j in range(len(lines[0])):
        curr_tallest = -1
        for i in range(len(lines)-1, 0, -1):
            if int(lines[i][j]) > curr_tallest:
                if (i, j) not in seen:
                    seen.add((i,j))
                    total_trees += 1
                curr_tallest = int(lines[i][j])

    print(total_trees)

main()
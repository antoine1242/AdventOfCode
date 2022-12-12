import math
import copy

def check_neighbours(grid, i, j, min_steps):
    result = False
    if i > 0:
        if not (grid[i][j] - grid[i-1][j] > 1) and min_steps[i-1][j] + 1 < min_steps[i][j]:
            min_steps[i][j] = min_steps[i-1][j] + 1
            result = True

    if j > 0:
        if not (grid[i][j] - grid[i][j-1] > 1) and min_steps[i][j-1] + 1 < min_steps[i][j]:
            min_steps[i][j] = min_steps[i][j-1] + 1
            result = True

    if i < len(grid)-1:
        if not (grid[i][j] - grid[i+1][j] > 1) and min_steps[i+1][j] + 1 < min_steps[i][j]:
            min_steps[i][j] = min_steps[i+1][j] + 1
            result = True

    if j < len(grid[0])-1:
        if not (grid[i][j] - grid[i][j+1] > 1) and min_steps[i][j+1] + 1 < min_steps[i][j]:
            min_steps[i][j] = min_steps[i][j+1] + 1
            result = True

    return result

def main():
    with open("Day12/input.txt") as f:
        lines = f.read().split("\n")

    grid = [list(line) for line in lines]

    starts = []
    end = [0,0]
    max = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].islower():
                ordinance = ord(grid[i][j])
                grid[i][j] = ordinance - 96
                if grid[i][j] > max:
                    max = grid[i][j]
                if ordinance - 96 == 1:
                    starts.append([i,j])

            elif grid[i][j] == "S":
                starts.append([i,j])
                grid[i][j] = 0
            elif grid[i][j] == "E":
                end = [i,j]
            
    grid[end[0]][end[1]] = max + 1

    shortest = 99999

    for start in starts:
        min_steps = [[9999999 for i in range(len(grid[0]))] for j in range(len(grid))]
        min_steps[start[0]][start[1]] = 0

        changed = True

        while changed:
            changed = False

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    result = check_neighbours(grid, i, j, min_steps)
                    if result:
                        changed = True

        if min_steps[end[0]][end[1]] < shortest:
            shortest = min_steps[end[0]][end[1]]

    print(shortest) # Prend 5-10 min à rouler
    
main()
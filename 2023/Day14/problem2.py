from aocd.models import Puzzle
import copy

def make_rock_cycle(grid):
    moved = True
    while moved:
        moved = False
        # move north
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and grid[i-1][j] == ".":
                    moved = True
                    grid[i][j] = "."
                    grid[i-1][j] = "O"

    moved = True
    while moved:
        moved = False
        # move west
        for i in range(len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == "O" and grid[i][j-1] == ".":
                    moved = True
                    grid[i][j] = "."
                    grid[i][j-1] = "O"

    moved = True
    while moved:
        moved = False
        # move south
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and grid[i+1][j] == ".":
                    moved = True
                    grid[i][j] = "."
                    grid[i+1][j] = "O"

    moved = True
    while moved:
        moved = False
        # move east
        for i in range(len(grid)):
            for j in range(len(grid[0])-1):
                if grid[i][j] == "O" and grid[i][j+1] == ".":
                    moved = True
                    grid[i][j] = "."
                    grid[i][j+1] = "O"
    
def count_weight_north(grid):
    weight = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                weight += len(grid) - i

    return weight

def main(test=False):
    if test:
        with open("Day14/input.txt") as f:
            lines = f.read()
    else:
        lines = Puzzle(year=2023, day=14).input_data

    lines = lines.split("\n")

    grid = []

    for line in lines:
        grid.append(list(line))

    grids = []
    grids.append(copy.deepcopy(grid))

    cycles = 0

    while True:
        make_rock_cycle(grid)
        
        cycles += 1

        if grid in grids:
            index = grids.index(grid)
            cycles_between = cycles - index
            break

        grids.append(copy.deepcopy(grid))

    remaining = (1000000000 - index) % cycles_between

    for i in range(remaining):
        make_rock_cycle(grid)

    print(count_weight_north(grid))

#main(test=True)
main() # 96105

import math
import copy

def move_east(grid):
    moved = False
    tmp_grid = copy.deepcopy(grid)
    width_grid = len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ">":
                if grid[i][(j+1) % width_grid] == ".":
                    moved = True
                    tmp_grid[i][j] = "."
                    tmp_grid[i][(j+1) % width_grid] = ">"

    return moved, tmp_grid

def move_south(grid):
    moved = False
    tmp_grid = copy.deepcopy(grid)
    height_grid = len(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "v":
                if grid[(i+1) % height_grid][j] == ".":
                    moved = True
                    tmp_grid[i][j] = "."
                    tmp_grid[(i+1) % height_grid][j] = "v"

    return moved, tmp_grid

def main():
    with open("input.txt") as f:
        grid = f.read().split("\n")

    for i in range(len(grid)):
        grid[i] = list(grid[i])

    moved = True
    moves = 0

    while moved:
        moved_east, grid = move_east(grid)
        moved_south, grid = move_south(grid)
        moved = moved_east or moved_south
        moves += 1

    print(moves)

main()
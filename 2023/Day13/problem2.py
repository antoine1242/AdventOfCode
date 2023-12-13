from aocd.models import Puzzle

def check_horizontal_reflexion(grid, j): 
    diffs = 0
    left = j - 1
    right = j

    while left >= 0 and right <= len(grid[0])-1:
        for i in range(len(grid)):
            if grid[i][left] != grid[i][right]:
                diffs += 1
        
        left -= 1
        right += 1

    return diffs == 1

def check_vertical_reflexion(grid, i):
    diffs = 0
    up = i - 1
    down = i

    while up >= 0 and down <= len(grid)-1:
        for j in range(len(grid[0])):
            if grid[down][j] != grid[up][j]:
                diffs += 1

        up -= 1
        down += 1

    return diffs == 1

def main(test=False):
    if test:
        with open("Day13/input.txt") as f:
            lines = f.read()
    else:
        lines = Puzzle(year=2023, day=13).input_data

    grids = lines.split("\n\n")

    verticals = 0
    horizontals = 0

    for grid in grids:
        grid = grid.split("\n")
        
        for i in range(1, len(grid)):
            if check_vertical_reflexion(grid, i):
                horizontals += i
                break

        for j in range(1, len(grid[0])):
            if check_horizontal_reflexion(grid, j):
                verticals += j
                break

    print(verticals + 100*horizontals)

main(test=True)
main() # 36919

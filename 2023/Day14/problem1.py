from aocd.models import Puzzle

def make_rock_go_north(grid):
    moved = True
    while moved:
        moved = False

        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and grid[i-1][j] == ".":
                    moved = True
                    grid[i][j] = "."
                    grid[i-1][j] = "O"
    
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

    make_rock_go_north(grid)
    print(count_weight_north(grid))

#main(test=True)
main() # 109596

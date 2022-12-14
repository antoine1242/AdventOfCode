import math
import copy

def draw_path(grid, path):
    for i in range(len(path)-1):
        # La ligne va être verticale
        if abs(path[i][0] - path[i+1][0]) > 0:
            y = path[i][1]

            if path[i][0] > path[i+1][0]:
                for x in range(path[i+1][0], path[i][0]+1):
                    grid[x][y] = "#"
            else:
                for x in range(path[i][0], path[i+1][0]+1):
                    grid[x][y] = "#"

        # La ligne va être horizontale
        elif abs(path[i][1] - path[i+1][1]) > 0:
            x = path[i][0]

            if path[i][1] > path[i+1][1]:
                for y in range(path[i+1][1], path[i][1]+1):
                    grid[x][y] = "#"
            else:
                for y in range(path[i][1], path[i+1][1]+1):
                    grid[x][y] = "#"

def generate_sand(grid, sand_start):
    x = sand_start[0]
    y = sand_start[1]

    moves = 0

    while True:
        while grid[x+1][y] == ".":
            x += 1
            moves += 1
            if moves == 2000:
                return True

        if grid[x+1][y-1] == ".":
            x += 1
            y -= 1
            moves += 1
        elif grid[x+1][y+1] == ".":
            x += 1
            y += 1
            moves += 1
        
        if grid[x+1][y] != "." and grid[x+1][y-1] != "." and grid[x+1][y+1] != ".":
            grid[x][y] = "o"
            return False
    

def main():
    with open("Day14/input.txt") as f:
        paths = f.read().split("\n")

    grid = [["." for j in range(1000)] for i in range(3000)]

    paths = [[x.split(",") for x in array] for array in [path.split(" -> ") for path in paths]]

    for i in range(len(paths)):
        for j in range(len(paths[i])):
            tmp = int(paths[i][j][0])
            paths[i][j][0] = int(paths[i][j][1])
            paths[i][j][1] = tmp 

    for path in paths:
        draw_path(grid, path)

    sand_start = [0, 500]

    sand_stop = False
    sands = -1

    while not sand_stop:
        sand_stop = generate_sand(grid, sand_start)
        sands += 1

    for i in range(10, 80):
        line = ""
        for j in range(450, 530):
            line += grid[i][j]
        print(line)

    print(sands)
    
main()

# 961 not good
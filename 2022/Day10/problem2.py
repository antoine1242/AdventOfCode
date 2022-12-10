import math
import copy

def draw_pixel(grid, cycle, register):
    curr_i = (cycle // 40)  # Pas sûr
    curr_j = (cycle % 40) - 1 # Pas sûr

    if abs(curr_j - register) <= 1:
        grid[curr_i][curr_j] = "#"
    else:
        grid[curr_i][curr_j] = "." 

def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    grid = [["X" for i in range(40)] for j in range(7)]

    register = 1
    cycle = 0

    for line in lines:
        op = line.split(" ")[0]

        if op != "noop":
            num = int(line.split(" ")[1])

        if op == "noop":
            cycle += 1
            draw_pixel(grid, cycle, register)

        else:
            cycle += 1
            draw_pixel(grid, cycle, register)

            cycle += 1
            draw_pixel(grid, cycle, register)

            register += num

    for row in grid:
        print(row)
    
main()
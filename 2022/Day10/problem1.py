import math
import copy

def main():
    with open("Day10/input.txt") as f:
        lines = f.read().split("\n")

    total = 0
    register = 1
    cycle = 0

    check = [20, 60, 100, 140, 180, 220]

    for line in lines:
        op = line.split(" ")[0]

        if op != "noop":
            num = int(line.split(" ")[1])

        if op == "noop":
            cycle += 1
            if cycle in check:
                total += register * cycle

        else:
            cycle += 1
            if cycle in check:
                total += register * cycle

            cycle += 1
            if cycle in check:
                total += register * cycle

            register += num

    print(total)
    
main()
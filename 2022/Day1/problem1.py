import math
import copy

def main():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")

    top_1 = sorted([sum([int(value) for value in array]) for array in [group.split("\n") for group in groups]])[::-1][0]
    print(top_1)

main()

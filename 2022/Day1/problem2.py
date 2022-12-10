import math
import copy

def main():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")

    calories_per_elf = [sum([int(value) for value in array]) for array in [group.split("\n") for group in groups]]
    calories_per_elf.sort()
    calories_per_elf.reverse()
    
    sum_top_3 = sum(calories_per_elf[0:3])
    print(sum_top_3)

main()

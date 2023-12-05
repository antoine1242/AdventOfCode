import math
import copy
import re

def main():
    with open("Day4/input.txt") as f:
        lines = f.read().split("\n")
    
    lines = [line for line in lines if line]

    matches_list = [1 for i in range(len(lines))]

    for index, line in enumerate(lines):
        winning_nums = line.split(" | ")[0].split(": ")[1].split(" ")
        winning_nums = [int(i) for i in winning_nums if i]

        my_nums = line.split(" | ")[1].split(" ")
        my_nums = [int(i) for i in my_nums if i]

        matches = 0

        for my_num in my_nums:
            if my_num in winning_nums:
                matches += 1

        for i in range(index+1, index+1+matches):
            matches_list[i] += matches_list[index]

    print(sum(matches_list))
main()
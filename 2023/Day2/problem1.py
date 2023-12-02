import math
import copy
import re


def main():
    with open("Day2/input.txt") as f:
        lines = f.read().split("\n")

    id_sum = 0
    # RGB
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
        
    for line in lines:
        possible = True

        game_id = int(line.split(":")[0].split(" ")[1])
        
        sets = line.split(":")[1].strip().split(";")

        for set_ in sets:
            colors = set_.strip().split(",")
            
            for color in colors:
                curr = color.strip()
                curr_color = curr.split(" ")[1]
                curr_number = int(curr.split(" ")[0])

                if max_cubes[curr_color] < curr_number:
                    possible = False
        if possible:
            id_sum += game_id

    print(id_sum)
main()
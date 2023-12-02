import math
import copy
import re

def main():
    with open("Day2/input.txt") as f:
        lines = f.read().split("\n")

    power_sum = 0
  
    for line in lines:
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        sets = line.split(":")[1].strip().split(";")

        for set_ in sets:
            colors = set_.strip().split(",")
            
            for color in colors:
                curr = color.strip()
                curr_color = curr.split(" ")[1]
                curr_number = int(curr.split(" ")[0])

                if min_cubes[curr_color] < curr_number:
                    min_cubes[curr_color] = curr_number
                
        power_sum += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    print(power_sum)
main()
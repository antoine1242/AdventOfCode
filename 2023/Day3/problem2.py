import math
import copy
import re

def char_touch(lines, j_, i_):
    for i in range(i_-1, i_+2):
        for j in range(j_-1, j_+2):
            if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[0]):
                if lines[i][j] == "*":
                    return str(i) + "," + str(j)
    return False

def touch_machine_part(lines, curr_num, id_line, id_char):
    touch = False

    for i in range(id_char-len(curr_num)+1, id_char+1):
        curr = char_touch(lines, i, id_line)
        if curr:
            return curr

    return False

def main():
    with open("Day3/input.txt") as f:
        lines = f.read().split("\n")

    touching_stars = {}

    for id_line, line in enumerate(lines):
        curr_num = ""

        for id_char, char in enumerate(line):
            if char.isdigit():
                curr_num += char
            elif len(curr_num) > 0:
                star_coordinates = touch_machine_part(lines, curr_num, id_line, id_char-1)
                if star_coordinates:
                    if star_coordinates in touching_stars:
                        touching_stars[star_coordinates].append(curr_num)
                    else:
                        touching_stars[star_coordinates] = [curr_num]
            
                curr_num = ""
        if len(curr_num) > 0:
            star_coordinates = touch_machine_part(lines, curr_num, id_line, len(line)-1)
            if star_coordinates:
                if star_coordinates in touching_stars:
                    touching_stars[star_coordinates].append(curr_num)
                else:
                    touching_stars[star_coordinates] = [curr_num]

    gear_ratios_sum = 0

    for key, value in touching_stars.items():
        if len(value) == 2:
            gear_ratios_sum += int(value[0]) * int(value[1])

    print(gear_ratios_sum)
main()
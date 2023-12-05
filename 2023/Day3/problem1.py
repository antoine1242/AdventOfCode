import math
import copy
import re

def char_touch(lines, j_, i_):
    for i in range(i_-1, i_+2):
        for j in range(j_-1, j_+2):
            if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[0]):
                if lines[i][j] != "." and not lines[i][j].isdigit():
                    return True
    return False

def touch_machine_part(lines, curr_num, id_line, id_char):
    touch = False

    for i in range(id_char-len(curr_num)+1, id_char+1):
        if char_touch(lines, i, id_line):
            touch = True
            break

    return touch

def main():
    with open("Day3/input.txt") as f:
        lines = f.read().split("\n")

    part_numbers_sum = 0

    for id_line, line in enumerate(lines):
        curr_num = ""

        for id_char, char in enumerate(line):
            if char.isdigit():
                curr_num += char
            elif len(curr_num) > 0:
                if touch_machine_part(lines, curr_num, id_line, id_char-1):
                    part_numbers_sum += int(curr_num)
            
                curr_num = ""
        if len(curr_num) > 0:
            if touch_machine_part(lines, curr_num, id_line, len(line)-1):
                part_numbers_sum += int(curr_num)

    print(part_numbers_sum)
main()
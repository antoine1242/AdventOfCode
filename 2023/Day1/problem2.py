import math
import copy
import re

three_chars_ints = ['one', 'two', 'six']
four_chars_ints = ['four', 'five', 'nine']
five_chars_ints = ['three', 'seven', 'eight']

char_int_dict = {'one': '1', 'two':  '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def main():
    with open("Day1/input.txt") as f:
        lines = f.read().split("\n")

    sum = 0

    for line in lines:
        number = ""
        for index, char in enumerate(line):
            if char.isdigit():
                number += char
                break
            elif line[index:index+3] in three_chars_ints:
                number += char_int_dict[line[index:index+3]]
                break
            elif line[index:index+4] in four_chars_ints:
                number += char_int_dict[line[index:index+4]]
                break
            elif line[index:index+5] in five_chars_ints:
                number += char_int_dict[line[index:index+5]]
                break
        
        reversed_line = line[::-1]
        for index, char in enumerate(reversed_line):
            if char.isdigit():
                number += char
                break
            elif reversed_line[index:index+3][::-1] in three_chars_ints:
                number += char_int_dict[reversed_line[index:index+3][::-1]]
                break
            elif reversed_line[index:index+4][::-1] in four_chars_ints:
                number += char_int_dict[reversed_line[index:index+4][::-1]]
                break
            elif reversed_line[index:index+5][::-1] in five_chars_ints:
                number += char_int_dict[reversed_line[index:index+5][::-1]]
                break

        sum += int(number)
    
    print(sum)

main()

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
        for char in line:
            if char.isdigit():
                number += char
                break
        
        reversed_line = line[::-1]
        for char in reversed_line:
            if char.isdigit():
                number += char
                break

        sum += int(number)
    
    print(sum)

main()

def word_to_digit(word):
    word_to_digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return ''.join(word_to_digit_mapping.get(char.lower(), char) for char in word)

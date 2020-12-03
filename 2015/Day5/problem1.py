import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    nice_strings = 0

    for entry in entries:
        if has_a_double(entry) and has_three_vowels(entry) and has_no_bad_double(entry):
            nice_strings += 1
        
    print(nice_strings)

def has_no_bad_double(entry):
    return ("ab" not in entry) and ("cd" not in entry) and ("pq" not in entry) and ("xy" not in entry)

def has_three_vowels(entry):
    vowels_count = 0
    
    for letter in entry:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            vowels_count += 1

    return vowels_count >= 3

def has_a_double(entry):
    for i in range(len(entry) - 1):
        if entry[i] == entry[i+1]:
            return True
    
    return False

main()
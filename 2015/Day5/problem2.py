import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    nice_strings = 0

    for entry in entries:
        if has_a_repeat(entry) and has_two_pairs(entry):
            nice_strings += 1
        
    print(nice_strings)

def has_two_pairs(entry):
    pairs = []
    
    for i in range(len(entry) - 1):
    	pair = entry[i:i+1]
    	if pair in pairs:
    		return True
    	else:
    		pairs.append(pair)

    return False

def has_a_repeat(entry):
    for i in range(len(entry) - 2):
        if entry[i] == entry[i + 2]:
            return True
    
    return False

main()
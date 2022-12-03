import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    numbers = [x.strip() for x in entries]

    max_global = 0

    curr_counter = 0

    for n in numbers:
        if len(n) == 0:
            if curr_counter > max_global:
                max_global = curr_counter
            curr_counter = 0
        else:
            curr_counter += int(n)
        
    if curr_counter > max_global:
        max_global = curr_counter

    print(max_global)
main()

#720660
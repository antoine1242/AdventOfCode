import math
import copy

def main():
    with open("input.txt") as f:
        entry = f.readline()

    current = 0
    i = 0
    while i < len(entry):
        if entry[i] == "(":
            current += 1
        else:
            current -= 1

        if current == -1:
            return i + 1
        
        i += 1

print(main())
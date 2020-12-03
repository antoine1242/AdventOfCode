import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    total = 0

    for entry in entries:
        total += extract_ribbon_size(entry)

    print(total)

def extract_ribbon_size(entry):
    sizes = entry.split("x")

    l = int(sizes[0])
    w = int(sizes[1])
    h = int(sizes[2])

    if l >= w and l >= h:
        return l*w*h + 2*w + 2*h
    elif w >= l and w >= h:
        return l*w*h + 2*l + 2*h
    else:
        return l*w*h + 2*l + 2*w        


main()
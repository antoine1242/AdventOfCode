import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    total = 0

    for entry in entries:
        total += extract_size(entry)

    print(total)

def extract_size(entry):
    sizes = entry.split("x")

    l = int(sizes[0])
    w = int(sizes[1])
    h = int(sizes[2])

    return 2*(l*w) + 2*(l*h) + 2*(h*w) + min(min(l*w, l*h), w*h)

main()
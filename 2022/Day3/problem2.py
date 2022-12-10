import math
import copy

def main():
    with open("Day3/input.txt") as f:
        # entries = f.read().split("\n\n")
        entries = f.read().split("\n")

    total = 0

    i = 0
    while i < len(entries):
        one = entries[i]
        two = entries[i+1]
        three = entries[i+2]

        common = ''.join(set(''.join(set(one).intersection(two))).intersection(three))

        if common.islower():
            total += (ord(common)-96)
        else:
            total += (ord(common)-38)

        i += 3

    print(total)


main()